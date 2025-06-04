import os
import subprocess
import socket


# Функция для получения текущего IP в локальной сети
def get_local_ip():
    try:
        # Используем HOST_IP из переменных окружения (если есть)
        if "HOST_IP" in os.environ:
            return os.environ["HOST_IP"]
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))  # Google DNS
                ip = s.getsockname()[0]
            return ip
    except Exception as e:
        print(f"Ошибка при определении IP: {e}")
        exit(1)


# Функция для сборки Docker образа
def build_docker_image(ip):
    try:

        # Запускаем сборку образа с передачей аргумента
        subprocess.run(
            [
                "docker", "build",
                "-t", "opencart-tests",
                "--build-arg", f"HOST_IP={ip}",
                "."
            ],
            check=True
        )
        print("Docker-образ успешно собран.")

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при сборке образа: {e}")
        exit(1)



# Функция для очистки Docker
def cleanup_docker(project_name="opencart_autotests"):
    try:
        # Удаляем контейнеры, связанные с проектом
        print("Удаляем контейнеры...")
        containers = subprocess.run(
            ["docker", "ps", "-qa", "--filter", f"name={project_name}"],
            stdout=subprocess.PIPE,
            text=True
        ).stdout.strip().split()

        if containers:
            for container in containers:
                subprocess.run(["docker", "rm", "-f", container], check=True)
                print(f"Контейнер {container} удален.")
        else:
            print("Контейнеры для удаления не найдены.")

        # Удаляем тома, связанные с проектом
        print("Удаляем тома...")
        volumes = subprocess.run(
            ["docker", "volume", "ls", "-q", "--filter", f"name={project_name}"],
            stdout=subprocess.PIPE,
            text=True
        ).stdout.strip().split()

        if volumes:
            for volume in volumes:
                subprocess.run(["docker", "volume", "rm", "-f", volume], check=True)
                print(f"Том {volume} удален.")
        else:
            print("Тома для удаления не найдены.")

        print("Очистка завершена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при очистке Docker: {e}")
        exit(1)


# Функция для запуска Docker Compose
def start_docker_compose(ip):
    try:
        # Устанавливаем переменную окружения LOCAL_IP
        env = os.environ.copy()
        env["LOCAL_IP"] = ip

        # Запускаем Docker Compose с установленной переменной окружения
        subprocess.run(["docker-compose", "up", "-d"], env=env, check=True)
        print("Docker Compose успешно запущен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при запуске Docker Compose: {e}")
        exit(1)


# Основная функция
def main():
    # Получаем IP
    ip = get_local_ip()
    print(f"Текущий IP в локальной сети: {ip}")

    # Собираем образ Docker с передачей нового IP в переменные окружения
    build_docker_image(ip)

    # Очищаем Docker
    for project_name in ("opencart", "mariadb"):
        cleanup_docker(project_name)

    # Запускаем Docker Compose с новым IP
    start_docker_compose(ip)


if __name__ == "__main__":
    main()
