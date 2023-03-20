# This file is automatically @generated by Poetry and should not be changed by hand.

[[package]]
name = "attrs"
version = "22.2.0"
description = "Classes Without Boilerplate"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "attrs-22.2.0-py3-none-any.whl", hash = "sha256:29e95c7f6778868dbd49170f98f8818f78f3dc5e0e37c0b1f474e3561b240836"},
    {file = "attrs-22.2.0.tar.gz", hash = "sha256:c9227bfc2f01993c03f68db37d1d15c9690188323c067c641f1a35ca58185f99"},
]

[package.extras]
cov = ["attrs[tests]", "coverage-enable-subprocess", "coverage[toml] (>=5.3)"]
dev = ["attrs[docs,tests]"]
docs = ["furo", "myst-parser", "sphinx", "sphinx-notfound-page", "sphinxcontrib-towncrier", "towncrier", "zope.interface"]
tests = ["attrs[tests-no-zope]", "zope.interface"]
tests-no-zope = ["cloudpickle", "cloudpickle", "hypothesis", "hypothesis", "mypy (>=0.971,<0.990)", "mypy (>=0.971,<0.990)", "pympler", "pympler", "pytest (>=4.3.0)", "pytest (>=4.3.0)", "pytest-mypy-plugins", "pytest-mypy-plugins", "pytest-xdist[psutil]", "pytest-xdist[psutil]"]

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
category = "dev"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]

[[package]]
name = "coverage"
version = "7.2.1"
description = "Code coverage measurement for Python"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "coverage-7.2.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:49567ec91fc5e0b15356da07a2feabb421d62f52a9fff4b1ec40e9e19772f5f8"},
    {file = "coverage-7.2.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:d2ef6cae70168815ed91388948b5f4fcc69681480a0061114db737f957719f03"},
    {file = "coverage-7.2.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3004765bca3acd9e015794e5c2f0c9a05587f5e698127ff95e9cfba0d3f29339"},
    {file = "coverage-7.2.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cca7c0b7f5881dfe0291ef09ba7bb1582cb92ab0aeffd8afb00c700bf692415a"},
    {file = "coverage-7.2.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b2167d116309f564af56f9aa5e75ef710ef871c5f9b313a83050035097b56820"},
    {file = "coverage-7.2.1-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:cb5f152fb14857cbe7f3e8c9a5d98979c4c66319a33cad6e617f0067c9accdc4"},
    {file = "coverage-7.2.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:87dc37f16fb5e3a28429e094145bf7c1753e32bb50f662722e378c5851f7fdc6"},
    {file = "coverage-7.2.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:e191a63a05851f8bce77bc875e75457f9b01d42843f8bd7feed2fc26bbe60833"},
    {file = "coverage-7.2.1-cp310-cp310-win32.whl", hash = "sha256:e3ea04b23b114572b98a88c85379e9e9ae031272ba1fb9b532aa934c621626d4"},
    {file = "coverage-7.2.1-cp310-cp310-win_amd64.whl", hash = "sha256:0cf557827be7eca1c38a2480484d706693e7bb1929e129785fe59ec155a59de6"},
    {file = "coverage-7.2.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:570c21a29493b350f591a4b04c158ce1601e8d18bdcd21db136fbb135d75efa6"},
    {file = "coverage-7.2.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:9e872b082b32065ac2834149dc0adc2a2e6d8203080501e1e3c3c77851b466f9"},
    {file = "coverage-7.2.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fac6343bae03b176e9b58104a9810df3cdccd5cfed19f99adfa807ffbf43cf9b"},
    {file = "coverage-7.2.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:abacd0a738e71b20e224861bc87e819ef46fedba2fb01bc1af83dfd122e9c319"},
    {file = "coverage-7.2.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d9256d4c60c4bbfec92721b51579c50f9e5062c21c12bec56b55292464873508"},
    {file = "coverage-7.2.1-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:80559eaf6c15ce3da10edb7977a1548b393db36cbc6cf417633eca05d84dd1ed"},
    {file = "coverage-7.2.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:0bd7e628f6c3ec4e7d2d24ec0e50aae4e5ae95ea644e849d92ae4805650b4c4e"},
    {file = "coverage-7.2.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:09643fb0df8e29f7417adc3f40aaf379d071ee8f0350ab290517c7004f05360b"},
    {file = "coverage-7.2.1-cp311-cp311-win32.whl", hash = "sha256:1b7fb13850ecb29b62a447ac3516c777b0e7a09ecb0f4bb6718a8654c87dfc80"},
    {file = "coverage-7.2.1-cp311-cp311-win_amd64.whl", hash = "sha256:617a94ada56bbfe547aa8d1b1a2b8299e2ec1ba14aac1d4b26a9f7d6158e1273"},
    {file = "coverage-7.2.1-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:8649371570551d2fd7dee22cfbf0b61f1747cdfb2b7587bb551e4beaaa44cb97"},
    {file = "coverage-7.2.1-cp37-cp37m-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5d2b9b5e70a21474c105a133ba227c61bc95f2ac3b66861143ce39a5ea4b3f84"},
    {file = "coverage-7.2.1-cp37-cp37m-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ae82c988954722fa07ec5045c57b6d55bc1a0890defb57cf4a712ced65b26ddd"},
    {file = "coverage-7.2.1-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:861cc85dfbf55a7a768443d90a07e0ac5207704a9f97a8eb753292a7fcbdfcfc"},
    {file = "coverage-7.2.1-cp37-cp37m-musllinux_1_1_aarch64.whl", hash = "sha256:0339dc3237c0d31c3b574f19c57985fcbe494280153bbcad33f2cdf469f4ac3e"},
    {file = "coverage-7.2.1-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:5928b85416a388dd557ddc006425b0c37e8468bd1c3dc118c1a3de42f59e2a54"},
    {file = "coverage-7.2.1-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:8d3843ca645f62c426c3d272902b9de90558e9886f15ddf5efe757b12dd376f5"},
    {file = "coverage-7.2.1-cp37-cp37m-win32.whl", hash = "sha256:6a034480e9ebd4e83d1aa0453fd78986414b5d237aea89a8fdc35d330aa13bae"},
    {file = "coverage-7.2.1-cp37-cp37m-win_amd64.whl", hash = "sha256:6fce673f79a0e017a4dc35e18dc7bb90bf6d307c67a11ad5e61ca8d42b87cbff"},
    {file = "coverage-7.2.1-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:7f099da6958ddfa2ed84bddea7515cb248583292e16bb9231d151cd528eab657"},
    {file = "coverage-7.2.1-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:97a3189e019d27e914ecf5c5247ea9f13261d22c3bb0cfcfd2a9b179bb36f8b1"},
    {file = "coverage-7.2.1-cp38-cp38-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a81dbcf6c6c877986083d00b834ac1e84b375220207a059ad45d12f6e518a4e3"},
    {file = "coverage-7.2.1-cp38-cp38-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:78d2c3dde4c0b9be4b02067185136b7ee4681978228ad5ec1278fa74f5ca3e99"},
    {file = "coverage-7.2.1-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3a209d512d157379cc9ab697cbdbb4cfd18daa3e7eebaa84c3d20b6af0037384"},
    {file = "coverage-7.2.1-cp38-cp38-musllinux_1_1_aarch64.whl", hash = "sha256:f3d07edb912a978915576a776756069dede66d012baa503022d3a0adba1b6afa"},
    {file = "coverage-7.2.1-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:8dca3c1706670297851bca1acff9618455122246bdae623be31eca744ade05ec"},
    {file = "coverage-7.2.1-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:b1991a6d64231a3e5bbe3099fb0dd7c9aeaa4275ad0e0aeff4cb9ef885c62ba2"},
    {file = "coverage-7.2.1-cp38-cp38-win32.whl", hash = "sha256:22c308bc508372576ffa3d2dbc4824bb70d28eeb4fcd79d4d1aed663a06630d0"},
    {file = "coverage-7.2.1-cp38-cp38-win_amd64.whl", hash = "sha256:b0c0d46de5dd97f6c2d1b560bf0fcf0215658097b604f1840365296302a9d1fb"},
    {file = "coverage-7.2.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:4dd34a935de268a133e4741827ae951283a28c0125ddcdbcbba41c4b98f2dfef"},
    {file = "coverage-7.2.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0f8318ed0f3c376cfad8d3520f496946977abde080439d6689d7799791457454"},
    {file = "coverage-7.2.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:834c2172edff5a08d78e2f53cf5e7164aacabeb66b369f76e7bb367ca4e2d993"},
    {file = "coverage-7.2.1-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e4d70c853f0546855f027890b77854508bdb4d6a81242a9d804482e667fff6e6"},
    {file = "coverage-7.2.1-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8a6450da4c7afc4534305b2b7d8650131e130610cea448ff240b6ab73d7eab63"},
    {file = "coverage-7.2.1-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:99f4dd81b2bb8fc67c3da68b1f5ee1650aca06faa585cbc6818dbf67893c6d58"},
    {file = "coverage-7.2.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:bdd3f2f285ddcf2e75174248b2406189261a79e7fedee2ceeadc76219b6faa0e"},
    {file = "coverage-7.2.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:f29351393eb05e6326f044a7b45ed8e38cb4dcc38570d12791f271399dc41431"},
    {file = "coverage-7.2.1-cp39-cp39-win32.whl", hash = "sha256:e2b50ebc2b6121edf352336d503357321b9d8738bb7a72d06fc56153fd3f4cd8"},
    {file = "coverage-7.2.1-cp39-cp39-win_amd64.whl", hash = "sha256:bd5a12239c0006252244f94863f1c518ac256160cd316ea5c47fb1a11b25889a"},
    {file = "coverage-7.2.1-pp37.pp38.pp39-none-any.whl", hash = "sha256:436313d129db7cf5b4ac355dd2bd3f7c7e5294af077b090b85de75f8458b8616"},
    {file = "coverage-7.2.1.tar.gz", hash = "sha256:c77f2a9093ccf329dd523a9b2b3c854c20d2a3d968b6def3b820272ca6732242"},
]

[package.extras]
toml = ["tomli"]

[[package]]
name = "iniconfig"
version = "2.0.0"
description = "brain-dead simple config-ini parsing"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "iniconfig-2.0.0-py3-none-any.whl", hash = "sha256:b6a85871a79d2e3b22d2d1b94ac2824226a63c6b741c88f7ae975f18b6778374"},
    {file = "iniconfig-2.0.0.tar.gz", hash = "sha256:2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3"},
]

[[package]]
name = "packaging"
version = "23.0"
description = "Core utilities for Python packages"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "packaging-23.0-py3-none-any.whl", hash = "sha256:714ac14496c3e68c99c29b00845f7a2b85f3bb6f1078fd9f72fd20f0570002b2"},
    {file = "packaging-23.0.tar.gz", hash = "sha256:b6ad297f8907de0fa2fe1ccbd26fdaf387f5f47c7275fedf8cce89f99446cf97"},
]

[[package]]
name = "pluggy"
version = "1.0.0"
description = "plugin and hook calling mechanisms for python"
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pluggy-1.0.0-py2.py3-none-any.whl", hash = "sha256:74134bbf457f031a36d68416e1509f34bd5ccc019f0bcc952c7b909d06b37bd3"},
    {file = "pluggy-1.0.0.tar.gz", hash = "sha256:4224373bacce55f955a878bf9cfa763c1e360858e330072059e10bad68531159"},
]

[package.extras]
dev = ["pre-commit", "tox"]
testing = ["pytest", "pytest-benchmark"]

[[package]]
name = "pytest"
version = "7.2.2"
description = "pytest: simple powerful testing with Python"
category = "dev"
optional = false
python-versions = ">=3.7"
files = [
    {file = "pytest-7.2.2-py3-none-any.whl", hash = "sha256:130328f552dcfac0b1cec75c12e3f005619dc5f874f0a06e8ff7263f0ee6225e"},
    {file = "pytest-7.2.2.tar.gz", hash = "sha256:c99ab0c73aceb050f68929bc93af19ab6db0558791c6a0715723abe9d0ade9d4"},
]

[package.dependencies]
attrs = ">=19.2.0"
colorama = {version = "*", markers = "sys_platform == \"win32\""}
iniconfig = "*"
packaging = "*"
pluggy = ">=0.12,<2.0"

[package.extras]
testing = ["argcomplete", "hypothesis (>=3.56)", "mock", "nose", "pygments (>=2.7.2)", "requests", "xmlschema"]

[[package]]
name = "pytest-cov"
version = "4.0.0"
description = "Pytest plugin for measuring coverage."
category = "dev"
optional = false
python-versions = ">=3.6"
files = [
    {file = "pytest-cov-4.0.0.tar.gz", hash = "sha256:996b79efde6433cdbd0088872dbc5fb3ed7fe1578b68cdbba634f14bb8dd0470"},
    {file = "pytest_cov-4.0.0-py3-none-any.whl", hash = "sha256:2feb1b751d66a8bd934e5edfa2e961d11309dc37b73b0eabe73b5945fee20f6b"},
]

[package.dependencies]
coverage = {version = ">=5.2.1", extras = ["toml"]}
pytest = ">=4.6"

[package.extras]
testing = ["fields", "hunter", "process-tests", "pytest-xdist", "six", "virtualenv"]

[metadata]
lock-version = "2.0"
python-versions = "^3.11"
content-hash = "a899065022ab97573ce8b3aa04bb77fa1ae8d5dccdf463ed5286bfa6b53a17dd"