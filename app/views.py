from . import main_bp


@main_bp.route('/', methods=['GET'])
def index():
    return {'message': 'This is main page'}
