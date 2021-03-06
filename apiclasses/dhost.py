import click
from apiclasses import common
from apiclasses import engine


@click.command(short_help='retrieve dhosts')
@common.add_options(common.dhostids)
@common.add_options(common.druleids)
@common.add_options(common.dserviceids)
# todo: for future use once we sort out passing queries
# @common.add_options(common.selectDRules)
# @common.add_options(common.selectDServices)
@common.add_options(common.limitSelects)
# todo: work out how to pass choices to DRY this
@click.option('--sortfield', type=click.Choice(['dhostid', 'druleid']))
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
def dhost(zart, sortfield, **kwargs):
    """This command retrieves dhosts."""
    zart.command = 'dhost'
    engine.engine(zart, sortfield, **kwargs)
