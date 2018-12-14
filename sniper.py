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


@console.command('invite')
@click.argument('invite_list', required=True)
def invite(invite_list):
    from core.Tasks import InviteTasks
    import asyncio
    tasks = InviteTasks()
    asyncio.run(tasks.create_tasks(invite_list=invite_list))


if __name__ == '__main__':
    click.secho(logo, fg='bright_green')
    console()
