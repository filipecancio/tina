from behave import given, when, then
from files import getStack,getPhotos

@given("It have some students waiting")
def given_stack(context):
    context.stack = getStack()
    assert context.stack != None

@then("It get all photographies from the camera")
def then_photos(context):
    context.photos = getPhotos()
    assert context.photos != None

@then("It get the spected a not null stack")
def then_limit_stack(context):
    context.lenStack = len(context.stack)
    assert context.stack != None

@then("It get the spected more then 2 students on the stack")
def then_limit_stack(context):
    context.lenStack = len(context.stack)
    assert context.lenStack > 2

@then("It get the spected less then 7 students on the stack")
def then_limit_stack(context):
    context.lenStack = len(context.stack)
    assert context.lenStack < 7

@then("It returns a stack of students photos")
def then_get_photos(context):
    for photo in context.stack:
        assert '.jpg' in photo