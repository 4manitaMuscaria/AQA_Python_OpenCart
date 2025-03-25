import logging


class LoggerManager:
    _instance = None

    @classmethod
    def get_logger(cls, log_level=logging.DEBUG, log_to_file=True, log_path=None, log_name="global_logger"):
        """
        Создаем глобальный логгер, если он еще не существует.
        Если уже существует, возвращаем существующий экземпляр.

        :param log_level: Уровень логирования
        :param log_to_file: Флаг записи в файл
        :param log_path: Путь к файлу логов
        :param log_name: Имя логгера
        :return: Объект логгера
        """
        if cls._instance is None:
            # Создаем новый логгер только один раз
            logger = logging.getLogger(log_name)
            logger.setLevel(log_level)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            if log_to_file:
                file_handler = logging.FileHandler(log_path, encoding="utf-8")
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

            cls._instance = logger

        return cls._instance
