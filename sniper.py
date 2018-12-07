import click
from core.logo import logo


@click.group()
def console():
    pass


@console.command('upload')
@click.option('--tag', '-t', default='test', help="tag标签：\n"
                                              "格式：category/tags\n"
                                              "如：tips/任意文件读取 或 ctf/web")
@click.argument('url', required=True)
def upload(url, tag):
    from core.Tasks import CommonTasks
    import asyncio
    tasks = CommonTasks()
    asyncio.run(tasks.create_tasks(url=url, tag=tag))


if __name__ == '__main__':
    click.secho(logo, fg='bright_green')
    console()
