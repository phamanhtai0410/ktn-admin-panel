from pydash import slugify

from src.views.base import MyBaseModelView, RowActionListMixin

from wtforms import validators


class NftRarityView(MyBaseModelView, RowActionListMixin):
    column_list = ['rarity_id', 'name', 'code', 'created_time']
    create_modal = True
    edit_modal = True
    # list_template = 'custom/nft_type.html'
    can_delete = False

    form_widget_args = {
        'code': {
            'readonly': True
        }
    }

    column_searchable_list = ['name']

    column_default_sort = ('rarity_id')

    def edit_form(self, obj=None):
        self.form_widget_args = {
            'code': {
                'readonly': True
            },
            'rarity_id': {
                'readonly': True
            }
        }
        return super(NftRarityView, self).edit_form(obj)

    def create_form(self, obj=None):
        self.form_widget_args = {
            'code': {
                'readonly': True
            }
        }
        return super(NftRarityView, self).edit_form(obj)

    def on_model_change(self, form, model, is_created):

        try:

            if is_created and not model.code:
                model.code = slugify(model.name).upper()

        except Exception as e:
            raise validators.ValidationError(e)
