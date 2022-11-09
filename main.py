from vk import VkClient
from db import SQLL3


# groups = VkClient().search_new_group()
groups = ((217071213123401, 'https://vk.com/club217071401', 'Шахтерск Днр магазин женской одежды'), (217070983, 'https://vk.com/club217070983', 'Naylo Bet | магазин одежды и обуви'))
# SQLL3().add_groups(tuple(map(lambda group: (group["id"], "https://vk.com/club" + str(group["id"]), group["name"]), groups)))
SQLL3().add_groups(groups)
print(groups, sep='\n')
