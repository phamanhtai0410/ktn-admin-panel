from markupsafe import Markup
from pydash import get

from src.connect import bsc
from src.views.base import MyBaseModelView, RowActionListMixin
from flask_admin import expose
from flask import request, redirect, render_template

from wtforms import validators


class NftTypeView(MyBaseModelView, RowActionListMixin):
    column_list = ['type_id', 'name', 'max_rarity','description', 'image', 'created_time']
    create_modal = True
    edit_modal = True
    # list_template = 'custom/nft_type.html'
    can_delete = False

    column_labels = {
        'type_id': 'Nft Type'
    }
    form_widget_args = {
        'type_id': {
            'disabled': True
        }
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
            'name': 'thanh',
            'rarity': 2,
            'is_active': True
        }
        print("------", nfts)
        return render_template('../../templates/custom/nft_type.html', nfts=nfts)

    def image_format(view, context, model, name):
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

    def on_model_change(self, form, model, is_created):

        try:

            if is_created:
                tx = bsc.smc_nft.functions.MAX_NFT_TYPE_VALUE().call()
                # print("MAX_NFT_TYPE_VALUE", tx, type(tx))
                # print("MAX_RARITY", form.max_rarity.data)
                _type_id = tx + 1
                model.type_id = _type_id
                tx = bsc.smc_nft.functions.addNewNftType(
                    bsc.toInt(text=str(_type_id)),
                    [bsc.toInt(text=str(form.max_rarity.data))]
                ).buildTransaction({
                    'gasPrice': bsc.eth.gas_price,
                    'nonce': bsc.eth.getTransactionCount(bsc.my_account.address)
                })

                signed_tx = bsc.my_account.signTransaction(tx)
                _txn = bsc.eth.send_raw_transaction(signed_tx.rawTransaction)

                _tx_hash = _txn.hex()
                _txn_receipt = bsc.eth.wait_for_transaction_receipt(_tx_hash)
                print(f"Log tx hash addNewNftType: {_tx_hash}")
                if get(_txn_receipt, 'status') != 1:
                    raise Exception(f"Failed: newType tx {_tx_hash}. Please re-check.")
            else:
                if self.max_rarity_before != form.max_rarity.data:
                    print('max_rarity_before', self.max_rarity_before)
                    if self.max_rarity_before and self.max_rarity_before > form.max_rarity.data:
                        raise Exception("Cannot reduce max rarity!")

                    tx = bsc.smc_nft.functions.upgradeExistingNftType(
                        bsc.toInt(text=str(form.type_id.data)),
                        bsc.toInt(text=str(form.max_rarity.data))
                    ).buildTransaction({
                        'gasPrice': bsc.eth.gas_price,
                        'nonce': bsc.eth.getTransactionCount(bsc.my_account.address)
                    })

                    signed_tx = bsc.my_account.signTransaction(tx)
                    _txn = bsc.eth.send_raw_transaction(signed_tx.rawTransaction)

                    _tx_hash = _txn.hex()
                    _txn_receipt = bsc.eth.wait_for_transaction_receipt(_tx_hash)
                    print(f"Log tx hash upgradeExistingNftType: {_tx_hash}")
                    if get(_txn_receipt, 'status') != 1:
                        raise Exception(f"Failed: newType tx {_tx_hash}. Please re-check.")
        except Exception as e:
            raise validators.ValidationError(e)

    def edit_form(self, obj=None):
        try:
            self.max_rarity_before = obj.max_rarity
        except AttributeError:
            pass

        return super(NftTypeView, self).edit_form(obj)
