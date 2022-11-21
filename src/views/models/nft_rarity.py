from pydash import slugify

from src.models.nft_collection import NftCollection
from src.views.base import MyBaseModelView, RowActionListMixin

from wtforms import validators, SelectField, HiddenField


class NftRarityView(MyBaseModelView, RowActionListMixin):
    column_list = ['rarity_id', 'name', 'collection_address', 'created_time']
    # create_modal = True
    edit_modal = True
    # list_template = 'custom/nft_type.html'
    can_delete = False

    form_widget_args = {
        'collection': {
            'readonly': True
        }
    }

    form_overrides = dict(
        collection_id=SelectField,
        collection_address=HiddenField
    )
    column_searchable_list = ['name']

    column_default_sort = ('rarity_id')

    def get_collections(self):
        return [(x.collection_id, x.name) for x in NftCollection.objects()]

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.collection_address = NftCollection.objects(collection_id=form.collection_id.data).first().address

    def edit_form(self, obj=None):
        self.form_widget_args = {
            'collection_id': {
                'readonly': True
            },
            'rarity_id': {
                'readonly': True
            }
        }
        _form = super(NftRarityView, self).edit_form(obj)

        _form = super(NftRarityView, self).edit_form(obj)
        _form.collection_id.choices = self.get_collections()
        return _form

    def create_form(self, obj=None):
        self.form_widget_args = {}
        _form = super(NftRarityView, self).edit_form(obj)
        _form.collection_id.choices = self.get_collections()
        return _form
