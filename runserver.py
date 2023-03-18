from API import create_app
from API.config.config import config_dict

import os

app = create_app(config=config_dict['prod'])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)