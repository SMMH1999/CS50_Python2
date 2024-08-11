"""Test File of project.py"""

import pytest
import project


data_obj = {"name": "App1", "username": "Username123", "password": "Password123"}
data_obj_copy = {"name": "App1", "username": "Username123", "password": "Password123"}
data_obj_new = {"name": "App2", "username": "Username123", "password": "Password123"}
data_obj_uniqe = {"name": "uniqe", "username": "Username123", "password": "Password123"}


@pytest.fixture
def empty_data():
    """empty_data Return empty dictionary

    Returns:
        obj: dict
    """
    obj = {}
    return obj


@pytest.fixture
def wrong_format_data():
    """wrong_format_data Return data with invalid format

    for example one (key,value) not acceptable

    Returns:
        obj: dict
    """
    obj = {
        "name": "reza",
        "email": "test@gmail.com",
        "password": "Password123",
    }
    return obj


@pytest.fixture
def wrong_size_data():
    """wrong_size_data Return data with invalid format size

    for example 4 (key,value) in dictionary

    Returns:
        obj: dict
    """
    obj = {
        "name": "App1",
        "password": "Password123",
    }
    return obj


def test_validate_add_item():
    """test_validate_add_item Testing Accepte data for add function"""
    # Testing Add empty obj
    with pytest.raises(ValueError, match=r"Your input is not enough"):
        project.add(empty_data)

    # Testing Add wrong format obj
    with pytest.raises(ValueError, match=r"Your input is not enough"):
        project.add(wrong_format_data)

    # Testing Add wrong size obj
    with pytest.raises(ValueError, match=r"Your input is not enough"):
        project.add(wrong_size_data)

    # Testing Add true obj
    assert project.add(data_obj) is True


def test_add_existed_item():
    """test_add_existed_item Test adding existed item"""
    # Add an item
    try:
        project.add(data_obj)
    except ValueError:
        assert ValueError("This information are existed")

    # Testing Add existed obj
    with pytest.raises(ValueError, match=r"This information are existed"):
        project.add(data_obj)


def test_edit_item():
    """test_edit_item Testing Edit function"""
    # Add an item
    try:
        project.add(data_obj)
    except ValueError:
        assert ValueError("This information are existed")

    # Testing Edit same Items
    with pytest.raises(
        ValueError, match=r"New information are the same last information"
    ):
        project.edit(data_obj, data_obj)

    # Testing Edit same objects
    with pytest.raises(
        ValueError, match=r"New information are the same last information"
    ):
        project.edit(data_obj, data_obj_copy)

    # Testing Edit not existed Item
    with pytest.raises(ValueError, match=r"Your information not existed !!"):
        project.edit(data_obj_uniqe, data_obj_new)


def test_validate_edit_item():
    """test_validate_edit_item Testing acceptable data for edit function"""
    # Add an item
    try:
        project.add(data_obj)
    except ValueError:
        assert ValueError("This information are existed")

    # Testing Edit empty obj
    with pytest.raises(ValueError, match=r"Your input not enough !!"):
        project.edit(data_obj, empty_data)

    # Testing Edit wrong format obj
    with pytest.raises(ValueError, match=r"Your input not enough !!"):
        project.edit(data_obj, wrong_format_data)

    # Testing Edit wrong size obj
    with pytest.raises(ValueError, match=r"Your input not enough !!"):
        project.edit(data_obj, wrong_size_data)


def test_validate_remove():
    """test_validate_remove Testing acceptable data for remove function"""
    # Add an item
    try:
        project.add(data_obj)
    except ValueError:
        assert ValueError("This information are existed")

    # Testing remove empty obj
    with pytest.raises(ValueError, match=r"Your information can not be empty !!"):
        project.remove(empty_data)

    # Testing remove wrong format obj
    with pytest.raises(ValueError, match=r"Your information can not be empty !!"):
        project.remove(wrong_format_data)

    # Testing remove wrong size obj
    with pytest.raises(ValueError, match=r"Your information can not be empty !!"):
        project.remove(wrong_size_data)


def test_remove_item():
    """test_remove_item Test remove function"""
    # Add an item
    try:
        project.add(data_obj)
    except ValueError:
        assert ValueError("This information are existed")

    # Testing remove not existed obj
    with pytest.raises(ValueError, match=r"Your information dose not exist"):
        project.remove(data_obj_new)

    # Testing remove item
    assert project.remove(data_obj_copy)


def test_show():
    """test_show Test show function with no information"""
    # Testing show the empty information list
    with pytest.raises(ValueError, match=r"The ledger is empty!!"):
        project.show()
