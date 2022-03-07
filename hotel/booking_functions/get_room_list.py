

def get_room_list():

    room = Room.objects.all()[0]
    room_list = []
    room_categories = dict(room.ROOM_CATEGORIES)

    for category in room_categories:
            room_category = room_categories.get(room_category)
            room_url = reverse('hotel:RoomDetailView', kwargs={
                            'category': room_category})

            room_list.append((room, room_url))
        context = {
            "room_list": room_list,
        }
    return room_list