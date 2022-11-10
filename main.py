from vk import VkClient
from db import SQLL3


def main():
    groups = VkClient().search_new_group("маркет", "магаз")
    SQLL3().add_groups(
        tuple(map(lambda group: (group["id"], "https://vk.com/club" + str(group["id"]), group["name"]), groups)))


if __name__ == "__main__":
    main()
