from behave import given, when, then
from menu import getRandomMenu

@given("It gotta some food options")
def given_gotta_food(context):
    context.menu = getRandomMenu()
    assert context.menu != None

@then("It choose a food option")
def then_food(context):
    assert context.menu["food"] != None

@then("It get a quantity of food unit")
def then_quantity(context):
    assert context.menu["quantity"] != None

@then("It get a limit of repetitions for student")
def then_limit(context):
    assert context.menu["limit"] != None

@then("It returns a menu object with all of this things")
def then_menu_ready(context):
    assert context.menu != None