# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

from __future__ import unicode_literals

from builtins import object


class BaseObject(object):
    __version__ = (0, 5, 0)
    __slots__ = []

    def __str__(self):
        return "<{} {}>".format(self.__class__.__name__, ", ".join(
            "{}={}".format(k, getattr(self, k)) for k in self.__slots__))


class ExceptionObject(Exception):
    __version__ = (0, 5, 0)
    __slots__ = []


class Connection(object):
    All = 0
    Resumable = 1
    Secure = 2


class DownloadState(object):
    All = 0
    Finished = 1
    Unfinished = 2
    Failed = 3
    Unmanaged = 4


class DownloadStatus(object):
    NA = 0
    Offline = 1
    Online = 2
    Queued = 3
    Paused = 4
    Finished = 5
    Skipped = 6
    Failed = 7
    Starting = 8
    Waiting = 9
    Downloading = 10
    TempOffline = 11
    Aborted = 12
    NotPossible = 13
    Missing = 14
    FileMismatch = 15
    Occupied = 16
    Decrypting = 17
    Processing = 18
    Custom = 19
    Unknown = 20


class FileStatus(object):
    Ok = 0
    Missing = 1
    Remote = 2


class InputType(object):
    NA = 0
    Text = 1
    Int = 2
    File = 3
    Folder = 4
    Textbox = 5
    Password = 6
    Time = 7
    TimeSpan = 8
    ByteSize = 9
    Bool = 10
    Click = 11
    Select = 12
    Multiple = 13
    List = 14
    PluginList = 15
    Table = 16


class Interaction(object):
    All = 0
    Notification = 1
    Captcha = 2
    Query = 4


class MediaType(object):
    All = 0
    Other = 1
    Audio = 2
    Image = 4
    Video = 8
    Document = 16
    Archive = 32
    Executable = 64


class PackageStatus(object):
    Ok = 0
    Paused = 1
    Folder = 2
    Remote = 3


class Permission(object):
    All = 0
    Add = 1
    Delete = 2
    Modify = 4
    Download = 8
    Accounts = 16
    Interaction = 32
    Plugins = 64


class ProgressType(object):
    All = 0
    Other = 1
    Download = 2
    Decrypting = 4
    LinkCheck = 8
    Addon = 16
    FileOperation = 32


class Role(object):
    Admin = 0
    User = 1


class AccountInfo(BaseObject):
    __slots__ = ['aid', 'plugin', 'loginname', 'owner', 'valid', 'validuntil',
                 'trafficleft', 'maxtraffic', 'premium', 'activated', 'shared', 'config']

    def __init__(self, aid=None, plugin=None, loginname=None, owner=None, valid=None, validuntil=None,
                 trafficleft=None, maxtraffic=None, premium=None, activated=None, shared=None, config=None):
        self.aid = aid
        self.plugin = plugin
        self.loginname = loginname
        self.owner = owner
        self.valid = valid
        self.validuntil = validuntil
        self.trafficleft = trafficleft
        self.maxtraffic = maxtraffic
        self.premium = premium
        self.activated = activated
        self.shared = shared
        self.config = config


class AddonInfo(BaseObject):
    __slots__ = ['name', 'description', 'value']

    def __init__(self, name=None, description=None, value=None):
        self.name = name
        self.description = description
        self.value = value


class AddonService(BaseObject):
    __slots__ = ['func_name', 'label',
                 'description', 'arguments', 'pack', 'media']

    def __init__(self, func_name=None, label=None, description=None,
                 arguments=None, pack=None, media=None):
        self.__name__ = func_name
        self.label = label
        self.description = description
        self.arguments = arguments
        self.pack = pack
        self.media = media


class ConfigHolder(BaseObject):
    __slots__ = ['name', 'label', 'description',
                 'explanation', 'items', 'info']

    def __init__(self, name=None, label=None, description=None,
                 explanation=None, items=None, info=None):
        self.name = name
        self.label = label
        self.description = description
        self.explanation = explanation
        self.items = items
        self.info = info


class ConfigInfo(BaseObject):
    __slots__ = ['name', 'label', 'description',
                 'category', 'user_context', 'activated']

    def __init__(self, name=None, label=None, description=None,
                 category=None, user_context=None, activated=None):
        self.name = name
        self.label = label
        self.description = description
        self.category = category
        self.user_context = user_context
        self.activated = activated


class ConfigItem(BaseObject):
    __slots__ = ['name', 'label', 'description', 'input', 'value']

    def __init__(self, name=None, label=None,
                 description=None, input=None, value=None):
        self.name = name
        self.label = label
        self.description = description
        self.input = input
        self.value = value


class Conflict(ExceptionObject):
    pass


class DownloadInfo(BaseObject):
    __slots__ = ['url', 'plugin', 'hash', 'status', 'statusmsg', 'error']

    def __init__(self, url=None, plugin=None, hash=None,
                 status=None, statusmsg=None, error=None):
        self.url = url
        self.plugin = plugin
        self.hash = hash
        self.status = status
        self.statusmsg = statusmsg
        self.error = error


class DownloadProgress(BaseObject):
    __slots__ = ['fid', 'pid', 'speed', 'conn', 'status']

    def __init__(self, fid=None, pid=None, speed=None, conn=None, status=None):
        self.fid = fid
        self.pid = pid
        self.speed = speed
        self.conn = conn
        self.status = status


class EventInfo(BaseObject):
    __slots__ = ['eventname', 'event_args']

    def __init__(self, eventname=None, event_args=None):
        self.eventname = eventname
        self.event_args = event_args


class FileDoesNotExist(ExceptionObject):
    __slots__ = ['fid']

    def __init__(self, fid=None):
        self.fid = fid


class FileInfo(BaseObject):
    __slots__ = ['fid', 'name', 'package', 'owner', 'size',
                 'status', 'media', 'added', 'fileorder', 'download']

    def __init__(self, fid=None, name=None, package=None, owner=None, size=None,
                 status=None, media=None, added=None, fileorder=None, download=None):
        self.fid = fid
        self.name = name
        self.package = package
        self.owner = owner
        self.size = size
        self.status = status
        self.media = media
        self.added = added
        self.fileorder = fileorder
        self.download = download


class Forbidden(ExceptionObject):
    pass


class Input(BaseObject):
    __slots__ = ['type', 'default_value', 'data']

    def __init__(self, type=None, default_value=None, data=None):
        self.type = type
        self.default_value = default_value
        self.data = data


class InteractionTask(BaseObject):
    __slots__ = ['iid', 'type', 'input', 'title', 'description', 'plugin']

    def __init__(self, iid=None, type=None, input=None,
                 title=None, description=None, plugin=None):
        self.iid = iid
        self.type = type
        self.input = input
        self.title = title
        self.description = description
        self.plugin = plugin


class InvalidConfigSection(ExceptionObject):
    __slots__ = ['section']

    def __init__(self, section=None):
        self.section = section


class LinkStatus(BaseObject):
    __slots__ = ['url', 'name', 'size', 'status', 'plugin', 'hash']

    def __init__(self, url=None, name=None, size=None,
                 status=None, plugin=None, hash=None):
        self.url = url
        self.name = name
        self.size = size
        self.status = status
        self.plugin = plugin
        self.hash = hash


class OnlineCheck(BaseObject):
    __slots__ = ['rid', 'data']

    def __init__(self, rid=None, data=None):
        self.rid = rid
        self.data = data


class PackageDoesNotExist(ExceptionObject):
    __slots__ = ['pid']

    def __init__(self, pid=None):
        self.pid = pid


class PackageInfo(BaseObject):
    __slots__ = ['pid', 'name', 'folder', 'root', 'owner', 'site', 'comment', 'password',
                 'added', 'tags', 'status', 'shared', 'packageorder', 'stats', 'fids', 'pids']

    def __init__(self, pid=None, name=None, folder=None, root=None, owner=None, site=None, comment=None, password=None,
                 added=None, tags=None, status=None, shared=None, packageorder=None, stats=None, fids=None, pids=None):
        self.pid = pid
        self.name = name
        self.folder = folder
        self.root = root
        self.owner = owner
        self.site = site
        self.comment = comment
        self.password = password
        self.added = added
        self.tags = tags
        self.status = status
        self.shared = shared
        self.packageorder = packageorder
        self.stats = stats
        self.fids = fids
        self.pids = pids


class PackageStats(BaseObject):
    __slots__ = ['linkstotal', 'linksdone', 'sizetotal', 'sizedone']

    def __init__(self, linkstotal=None, linksdone=None,
                 sizetotal=None, sizedone=None):
        self.linkstotal = linkstotal
        self.linksdone = linksdone
        self.sizetotal = sizetotal
        self.sizedone = sizedone


class ProgressInfo(BaseObject):
    __slots__ = ['plugin', 'name', 'statusmsg', 'eta',
                 'done', 'total', 'owner', 'type', 'download']

    def __init__(self, plugin=None, name=None, statusmsg=None, eta=None,
                 done=None, total=None, owner=None, type=None, download=None):
        self.plugin = plugin
        self.name = name
        self.statusmsg = statusmsg
        self.eta = eta
        self.done = done
        self.total = total
        self.owner = owner
        self.type = type
        self.download = download


class ServiceDoesNotExist(ExceptionObject):
    __slots__ = ['plugin', 'func']

    def __init__(self, plugin=None, func=None):
        self.plugin = plugin
        self.func = func


class ServiceException(ExceptionObject):
    __slots__ = ['msg']

    def __init__(self, msg=None):
        self.msg = msg


class StatusInfo(BaseObject):
    __slots__ = ['speed', 'linkstotal', 'linksqueue', 'sizetotal',
                 'sizequeue', 'notifications', 'paused', 'download', 'reconnect', 'quota']

    def __init__(self, speed=None, linkstotal=None, linksqueue=None, sizetotal=None, sizequeue=None,
                 notifications=None, paused=None, download=None, reconnect=None, quota=None):
        self.speed = speed
        self.linkstotal = linkstotal
        self.linksqueue = linksqueue
        self.sizetotal = sizetotal
        self.sizequeue = sizequeue
        self.notifications = notifications
        self.paused = paused
        self.download = download
        self.reconnect = reconnect
        self.quota = quota


class TreeCollection(BaseObject):
    __slots__ = ['root', 'files', 'packages']

    def __init__(self, root=None, files=None, packages=None):
        self.root = root
        self.files = files
        self.packages = packages


class Unauthorized(ExceptionObject):
    pass


class UserData(BaseObject):
    __slots__ = ['uid', 'name', 'email', 'role', 'permission', 'folder',
                 'traffic', 'dllimit', 'dlquota', 'hddquota', 'user', 'templatename']

    def __init__(self, uid=None, name=None, email=None, role=None, permission=None, folder=None,
                 traffic=None, dllimit=None, dlquota=None, hddquota=None, user=None, templatename=None):
        self.uid = uid
        self.name = name
        self.email = email
        self.role = role
        self.permission = permission
        self.folder = folder
        self.traffic = traffic
        self.dllimit = dllimit
        self.dlquota = dlquota
        self.hddquota = hddquota
        self.user = user
        self.templatename = templatename


class UserDoesNotExist(ExceptionObject):
    __slots__ = ['user']

    def __init__(self, user=None):
        self.user = user


class Iface(object):

    def add_links(self, pid, links):
        pass

    def add_local_file(self, pid, name, path):
        pass

    def add_package(self, name, links, password):
        pass

    def add_package_child(self, name, links, password, root, paused):
        pass

    def addPackageP(self, name, links, password, paused):
        pass

    def add_user(self, username, password):
        pass

    def check_container(self, filename, data):
        pass

    def check_html(self, html, url):
        pass

    def check_links(self, links):
        pass

    def create_account(self, plugin, loginname, password):
        pass

    def create_package(self, name, folder, root,
                       password, site, comment, paused):
        pass

    def delete_config(self, plugin):
        pass

    def delete_files(self, fids):
        pass

    def delete_packages(self, pids):
        pass

    def find_files(self, pattern):
        pass

    def find_packages(self, tags):
        pass

    def avail_space(self):
        pass

    def generate_download_link(self, fid, timeout):
        pass

    def generate_packages(self, links):
        pass

    def get_account_info(self, aid, plugin, refresh):
        pass

    def get_account_types(self):
        pass

    def get_accounts(self):
        pass

    def get_addon_handler(self):
        pass

    def get_all_files(self):
        pass

    def get_all_info(self):
        pass

    def get_all_user_data(self):
        pass

    def get_available_plugins(self):
        pass

    def get_config(self):
        pass

    def get_config_value(self, section, option):
        pass

    def get_core_config(self):
        pass

    def get_file_info(self, fid):
        pass

    def get_file_tree(self, pid, full):
        pass

    def get_filtered_file_tree(self, pid, full, state):
        pass

    def get_filtered_files(self, state):
        pass

    def get_info_by_plugin(self, plugin):
        pass

    def get_interaction_tasks(self, mode):
        pass

    def get_log(self, offset):
        pass

    def get_package_content(self, pid):
        pass

    def get_package_info(self, pid):
        pass

    def get_plugin_config(self):
        pass

    def get_progress_info(self):
        pass

    def get_quota(self):
        pass

    def get_server_version(self):
        pass

    def get_status_info(self):
        pass

    def get_user_data(self):
        pass

    def get_ws_address(self):
        pass

    def invoke_addon(self, plugin, func, func_args):
        pass

    def invoke_addon_handler(self, plugin, func, pid_or_fid):
        pass

    def is_interaction_waiting(self, mode):
        pass

    def load_config(self, name):
        pass

    def login(self, username, password):
        pass

    def move_files(self, fids, pid):
        pass

    def move_package(self, pid, root):
        pass

    def order_files(self, fids, pid, position):
        pass

    def order_package(self, pids, position):
        pass

    def parse_links(self, links):
        pass

    def pause_server(self):
        pass

    def poll_results(self, rid):
        pass

    def shutdown(self):
        pass

    def recheck_package(self, pid):
        pass

    def remove_account(self, account):
        pass

    def remove_files(self, fids):
        pass

    def remove_packages(self, pids):
        pass

    def remove_user(self, uid):
        pass

    def restart(self):
        pass

    def restart_failed(self):
        pass

    def restart_file(self, fid):
        pass

    def restart_package(self, pid):
        pass

    def save_config(self, config):
        pass

    def search_suggestions(self, pattern):
        pass

    def set_config_value(self, section, option, value):
        pass

    def set_interaction_result(self, iid, result):
        pass

    def set_package_paused(self, pid, paused):
        pass

    def set_password(self, username, old_password, new_password):
        pass

    def stop_all_downloads(self):
        pass

    def stop_downloads(self, fids):
        pass

    def toggle_pause(self):
        pass

    def toggle_reconnect(self):
        pass

    def unpause_server(self):
        pass

    def update_account(self, aid, plugin, loginname, password):
        pass

    def update_account_info(self, account):
        pass

    def update_package(self, pack):
        pass

    def update_user_data(self, data):
        pass

    def upload_container(self, filename, data):
        pass
