from dataset.repository.csv_repository import CSVDatasetRepository
from dataset.service.pagination_service import CSVPaginationService
from shared.const import Command
from renderer import render_page


def main():
    repo = CSVDatasetRepository("dataset_full.csv")
    service = CSVPaginationService(repo)

    current_page = 0
    page_size = 5

    total_pages = service.get_total_pages(page_size)

    print("write 'help' for command list.")
    while True:
        cmd = input(">> ").strip().lower()

        match cmd:
            case Command.HELP.value:
                print("show - to show all the data")
                print("next - to go to next page")
                print("prev - to go back to previous page")
            case Command.SHOW.value:
                rows = service.get_page(current_page, page_size)
                render_page(rows, current_page, total_pages)
                
            case Command.NEXT.value:
                if current_page + 1 < total_pages:
                    current_page += 1
                    rows = service.get_page(current_page, page_size)
                    render_page(rows, current_page, total_pages)
                else:
                    print("Already on the last page")
            case Command.PREV.value:
                current_page = max(0,current_page-1)
            case _:
                print("unknown commands. write 'help' for command list.")


if __name__ == "__main__":
    main()
