from todobien.models.models import Task


class Crud:
    async def create(self, task: Task):
        await task.save()
        return task

    async def read(self, pk: int):
        return await Task.objects.get(pk=pk)

    async def read_by_name(self, name: str):
        return await Task.objects.get(name=name)
