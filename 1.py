import queue
import time

request_queue = queue.Queue()


def generate_request(request_counter):
    request_id = f"#{request_counter}"
    request_queue.put(request_id)
    print(f"Заявку {request_id} додано до черги.")


def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки {request_id}...")
        time.sleep(1)
        print(f"Заявку {request_id} оброблено.")
    else:
        print("Черга пуста. Немає заявок для обробки.")


def main():
    request_counter = 1

    max_requests = 5

    while request_counter <= max_requests:
        generate_request(request_counter)

        process_request()

        time.sleep(1)

        request_counter += 1

    print("Досягнуто максимальну кількість заявок. Програма завершена.")


if __name__ == "__main__":
    main()