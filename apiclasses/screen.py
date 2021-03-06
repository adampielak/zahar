import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve screens')
@common.add_options(common.screenids)
@common.add_options(common.userids)
@common.add_options(common.screenitemids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectUsers)
# @common.add_options(common.selectUserGroups)
# @common.add_options(common.selectScreenItems)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['screenid', 'name']))
@common.add_options(common.countOutput)
@common.add_options(common.editable)
@common.add_options(common.excludeSearch)
@common.add_options(common.filter)
@common.add_options(common.limit)
@common.add_options(common.output)
@common.add_options(common.preservekeys)
@common.add_options(common.search)
@common.add_options(common.searchByAny)
@common.add_options(common.searchWildcardsEnabled)
@common.add_options(common.sortorder)
@common.add_options(common.startSearch)
@common.add_options(common.outputformat)
@click.pass_obj
def screen(zart, sortfield, **kwargs):
    """This command retrieves screens."""
    zart.command = 'screen'
    engine.engine(zart, sortfield, **kwargs)
