# BrowserStack DesiredCapabilities Dict
# Each dictionary entry is a desiredCapabilities description for a particular configuration supported by BrowserStack
# or a local Docker container
# TODO add more Windows versions, OSX and mobile browsers IAT-58
browsers = {
    'local': {
        'browserName': 'Chrome',
    },
    'chrome_latest': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1600x1200',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Chrome',
    },
    'chrome_previous': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Chrome',
        'browser_version': '81.0',
    },
    'chrome_1y': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Chrome',
        'browser_version': '73.0',
    },
    'chrome_3y': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Chrome',
        'browser_version': '58.0',
    },
    'edge_latest': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Edge',
    },
    'edge_previous': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Edge',
        'browser_version': '81.0',
    },
    'edge_1y': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Edge',
        'browser_version': '18.0',
    },
    'edge_3y': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'Edge',
        'browser_version': '15.0',
    },
    'ie_11': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.5.2',
        },
        'browserName': 'IE',
        'browserVersion': '11.0',
    },
    'firefox_latest': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.10.0',
        },
        'browserName': 'Firefox',
    },
    'firefox_previous': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.10.0',
        },
        'browserName': 'Firefox',
        'browserVersion': '76.0',
    },
    'firefox_1y': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.10.0',
        },
        'browserName': 'Firefox',
        'browserVersion': '66.0'
    },
    'firefox_3y': {
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.10.0',
        },
        'browserName': 'Firefox',
        'browserVersion': '52.0'
    },
    "safari_latest": {
        'bstack:options': {
            'os': 'OS X',
            'osVersion': 'Mojave',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.13.0',
        },
        'browserName': 'Safari',
    },
    "safari_1y": {
        'bstack:options': {
            'os': 'OS X',
            'osVersion': 'Sierra',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.13.0',
        },
        'browserName': 'Safari',
        'browserVersion': '12.1'
    },
    "safari_3y": {
        'bstack:options': {
            'os': 'OS X',
            'osVersion': 'Sierra',
            'resolution': '1280x1024',
            'local': 'false',
            'seleniumVersion': '3.13.0',
        },
        'browserName': 'Safari',
        'browserVersion': '10.1'
    }

}

