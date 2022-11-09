from vk import VkClient


groups = VkClient().search_new_group()
print(groups, sep='\n')
