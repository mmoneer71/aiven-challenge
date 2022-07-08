from consumer.service import create_message, get_message_by_id, get_messages_count


def test_create_message():
    old_count = get_messages_count()
    new_msg = create_message("random_msg")
    assert new_msg.text == "random_msg"
    assert get_message_by_id(new_msg.id) == new_msg
    assert get_messages_count() == old_count + 1


def test_empty_message():
    old_count = get_messages_count()
    new_msg = create_message("")
    assert not new_msg
    assert get_messages_count() == old_count


def test_invalid_id():
    assert not get_message_by_id("random")
