from Products.CMFCore.utils import getToolByName

skins = {
    'models.cellml.org': 'CellML Theme (models)',
    'models.physiomeproject.org': 'CellML Theme (PMR2)',
}

def select_theme(obj, event):
    server_url = event.request['SERVER_URL']
    host = server_url.split('://')[1].split(':')[0]
    skin = skins.get(host)
    if skin:
        site = getToolByName(obj, 'portal_url').getPortalObject()
        site.changeSkin(skin, event.request)
