import base64

wiz = env['product.image.import.wizard'].create({'folder_path': '/your/folder/path'})
print(wiz._normalize_key("Gift Card"))       # should print: gift card
print(wiz._normalize_key("gift_card.jpg"))   # should print: gift card

# Now assign manually
prod = env['product.template'].search([('name', '=', 'Gift Card')], limit=1)
with open('/your/folder/path/gift_card.jpg', 'rb') as f:
    prod.image_1920 = base64.b64encode(f.read())
