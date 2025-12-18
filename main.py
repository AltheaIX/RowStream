from dataset.repository.repository import CSVDatasetRepository
from dataset.service import CSVDatasetService
from shared.const import Command
from renderer import render_page


def get_validated_input(prompt, data_type=str):
    raw_input = input(prompt).strip()

    if not raw_input:
        return None

    try:
        return data_type(raw_input)
    except ValueError:
        print(f"⚠️ Error: Invalid input '{raw_input}'. Expected a valid {data_type.__name__}.")
        raise ValueError
    except TypeError:
        print(f"⚠️ Error: Invalid conversion attempt.")
        raise TypeError


def main():
    repo = CSVDatasetRepository("dataset_full.csv")
    service = CSVDatasetService(repo)

    current_page = 0
    page_size = 1

    total_pages = service.get_total_pages(page_size)

    print("write 'help' for command list.")
    while True:
        cmd = input(">> ").strip().lower()
        cmd_parts = cmd.split()

        match cmd_parts:
            case [Command.HELP.value]:
                print("create - to create a new data")
                print("show - to show all the data")
                print("update [number] - to update a data")
                print("delete [number] - to delete an existing data")
                print("jump [number] - to jump straight to the desired page")
                print("next - to go to next page")
                print("prev - to go back to previous page")
            case [Command.CREATE.value]:
                data_row = {}

                data_row['id'] = int(input("Enter ID: "))
                data_row['nama'] = input("Enter Nama: ")
                data_row['umur'] = int(input("Enter Umur: "))
                data_row['gender'] = input("Enter Gender: ")
                data_row['matkul'] = input("Enter Matkul: ")
                data_row['tanggal'] = input("Enter Tanggal: ")
                data_row['uts'] = float(input("Enter UTS: "))
                data_row['uas'] = float(input("Enter UAS: "))
                data_row['nilai'] = float(data_row['uts'] + data_row['uas']) / 2

                service.create_row(data_row)
                total_pages = service.get_total_pages(page_size)

                print(f"Creating data has success")
            case [Command.SHOW.value]:
                rows = service.get_page(current_page, page_size)
                render_page(rows, current_page, total_pages)
            case [Command.UPDATE.value, index]:
                data_row = {}

                try:
                    index_to_update = int(index)

                    print("Leave blank to keep the current data.")
                    data_row['nama'] = get_validated_input("Enter Nama: ")
                    data_row['gender'] = get_validated_input("Enter Gender: ")
                    data_row['matkul'] = get_validated_input("Enter Matkul: ")
                    data_row['tanggal'] = get_validated_input("Enter Tanggal (YYYY-MM-DD): ")
                    data_row['umur'] = get_validated_input("Enter Umur: ", data_type=int)
                    data_row['uts'] = get_validated_input("Enter UTS: ", data_type=float)
                    data_row['uas'] = get_validated_input("Enter UAS: ", data_type=float)

                    service.update_row(index_to_update, data_row)
                except ValueError:
                    continue
                except TypeError:
                    continue

            case [Command.DELETE.value, index]:
                try:
                    index_to_delete = int(index)
                    service.delete_row(index_to_delete)
                    total_pages = service.get_total_pages(page_size)

                    print(f"Deleting data with index {index} has success.")
                except ValueError:
                    print(f"Error: '{index}' is an invalid number.")
            case [Command.JUMP.value, page]:
                try:
                    new_page = int(page)

                    if new_page > total_pages or new_page < 0:
                        print("Page not found.")
                        continue

                    current_page = new_page-1

                    rows = service.get_page(current_page, page_size)
                    render_page(rows, current_page, total_pages)
                except ValueError:
                    print(f"Error: '{page}' is invalid for JUMP.")
            case [Command.NEXT.value]:
                if current_page + 1 < total_pages:
                    current_page += 1
                    rows = service.get_page(current_page, page_size)
                    render_page(rows, current_page, total_pages)
                else:
                    print("Already on the last page")
            case [Command.PREV.value]:
                current_page = max(0,current_page-1)
                rows = service.get_page(current_page, page_size)
                render_page(rows, current_page, total_pages)
            case _:
                print("unknown commands. write 'help' for command list.")


if __name__ == "__main__":
    main()
