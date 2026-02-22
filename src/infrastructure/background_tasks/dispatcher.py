from src.infrastructure.background_tasks.app import celery_app


class TasksDispatcher:
    def dispatch_upload_file(self, file_key, file_data):
        celery_app.send_task(
            "tasks.upload_file",
            args=[file_key, file_data]
        )
