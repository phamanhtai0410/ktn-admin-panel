from markupsafe import Markup
from src.views.base import MyBaseModelView, RowActionListMixin
from flask_admin import expose
from flask import request, redirect, render_template
import string
from src.models.nft_type import NftType
class NftTypeView(MyBaseModelView, RowActionListMixin):
    column_list = ['collection_id', 'name', 'description', 'image', 'created_time']
    create_modal = True
    edit_modal = True
    list_template = 'custom/nft_type.html'

    
    column_labels = {
        'collection_id': 'Nft Type'
    }
    
    @expose('/nft_show', methods=['POST'])
    def nft_show(self):
        # quantity = int(request.form['quantity'])
        # discount = int(request.form['discount'])
        # length = 8

        # for i in range(quantity):
        #     letters = string.ascii_uppercase + string.digits
        #     code = ''.join(random.choice(letters) for i in range(length))
            # NftType(code=code, discount=discount, status=True).save()

        return redirect('/nfttype/')
    
    @expose('/get_nft_detail', methods=['GET'])
    def get_nft_detail(self):
        _collection_id = int(request.form['collection_id'])
        # nfts = NftType.objects(collection_id= _collection_id)
        nfts = {
            'nft_id': 1,
            'name':'thanh',
            'rarity': 2,
            'is_active': True
        }
        print("------", nfts)
        return render_template('../../templates/custom/nft_type.html', nfts = nfts)
    
    
    def image_format( view, context, model , name):
        # _image = model['image']
        return Markup(f'<a target="_blank" href="{model["image"]}"> image </a>')

    
    # def items_view(view, context, model , name):
    #     return Markup(f'<button class="btn btn-success">Info</button>')
    
    column_searchable_list = ['name']

    column_default_sort = ('created_time', True)
    column_formatters = {
        'image': image_format,
        # 'view': items_view
    }

