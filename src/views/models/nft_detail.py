from src.views.base import MyBaseModelView


class NftDetailView(MyBaseModelView):
    column_list = ['nft_id', 'name', 'rarity', 'type', 'description', 'image', 'price']
    can_edit = False
    can_create = False
    can_delete = False

    column_searchable_list = ['name']

    column_default_sort = ('nft_id', False)

