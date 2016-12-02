#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autogenerated by pyload
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

class BaseObject(object):
	__version__ = (0, 4, 9, 9)
	__slots__ = []

	def __str__(self):
		return "<%s %s>" % (self.__class__.__name__, ", ".join("%s=%s" % (k,getattr(self,k)) for k in self.__slots__))

class ExceptionObject(Exception):
	__version__ = (0, 4, 9, 9)
	__slots__ = []

class Connection:
	All = 0
	Resumable = 1
	Secure = 2

class DownloadState:
	All = 0
	Finished = 1
	Unfinished = 2
	Failed = 3
	Unmanaged = 4

class DownloadStatus:
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

class FileStatus:
	Ok = 0
	Missing = 1
	Remote = 2

class InputType:
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

class Interaction:
	All = 0
	Notification = 1
	Captcha = 2
	Query = 4

class MediaType:
	All = 0
	Other = 1
	Audio = 2
	Image = 4
	Video = 8
	Document = 16
	Archive = 32
	Executable = 64

class PackageStatus:
	Ok = 0
	Paused = 1
	Folder = 2
	Remote = 3

class Permission:
	All = 0
	Add = 1
	Delete = 2
	Modify = 4
	Download = 8
	Accounts = 16
	Interaction = 32
	Plugins = 64

class ProgressType:
	All = 0
	Other = 1
	Download = 2
	Decrypting = 4
	LinkCheck = 8
	Addon = 16
	FileOperation = 32

class Role:
	Admin = 0
	User = 1

class AccountInfo(BaseObject):
	__slots__ = ['aid', 'plugin', 'loginname', 'owner', 'valid', 'validuntil', 'trafficleft', 'maxtraffic', 'premium', 'activated', 'shared', 'config']

	def __init__(self, aid=None, plugin=None, loginname=None, owner=None, valid=None, validuntil=None, trafficleft=None, maxtraffic=None, premium=None, activated=None, shared=None, config=None):
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
	__slots__ = ['func_name', 'label', 'description', 'arguments', 'pack', 'media']

	def __init__(self, func_name=None, label=None, description=None, arguments=None, pack=None, media=None):
		self.func_name = func_name
		self.label = label
		self.description = description
		self.arguments = arguments
		self.pack = pack
		self.media = media

class ConfigHolder(BaseObject):
	__slots__ = ['name', 'label', 'description', 'explanation', 'items', 'info']

	def __init__(self, name=None, label=None, description=None, explanation=None, items=None, info=None):
		self.name = name
		self.label = label
		self.description = description
		self.explanation = explanation
		self.items = items
		self.info = info

class ConfigInfo(BaseObject):
	__slots__ = ['name', 'label', 'description', 'category', 'user_context', 'activated']

	def __init__(self, name=None, label=None, description=None, category=None, user_context=None, activated=None):
		self.name = name
		self.label = label
		self.description = description
		self.category = category
		self.user_context = user_context
		self.activated = activated

class ConfigItem(BaseObject):
	__slots__ = ['name', 'label', 'description', 'input', 'value']

	def __init__(self, name=None, label=None, description=None, input=None, value=None):
		self.name = name
		self.label = label
		self.description = description
		self.input = input
		self.value = value

class Conflict(ExceptionObject):
	pass

class DownloadInfo(BaseObject):
	__slots__ = ['url', 'plugin', 'hash', 'status', 'statusmsg', 'error']

	def __init__(self, url=None, plugin=None, hash=None, status=None, statusmsg=None, error=None):
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
	__slots__ = ['fid', 'name', 'package', 'owner', 'size', 'status', 'media', 'added', 'fileorder', 'download']

	def __init__(self, fid=None, name=None, package=None, owner=None, size=None, status=None, media=None, added=None, fileorder=None, download=None):
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

	def __init__(self, iid=None, type=None, input=None, title=None, description=None, plugin=None):
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

	def __init__(self, url=None, name=None, size=None, status=None, plugin=None, hash=None):
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
	__slots__ = ['pid', 'name', 'folder', 'root', 'owner', 'site', 'comment', 'password', 'added', 'tags', 'status', 'shared', 'packageorder', 'stats', 'fids', 'pids']

	def __init__(self, pid=None, name=None, folder=None, root=None, owner=None, site=None, comment=None, password=None, added=None, tags=None, status=None, shared=None, packageorder=None, stats=None, fids=None, pids=None):
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

	def __init__(self, linkstotal=None, linksdone=None, sizetotal=None, sizedone=None):
		self.linkstotal = linkstotal
		self.linksdone = linksdone
		self.sizetotal = sizetotal
		self.sizedone = sizedone

class ProgressInfo(BaseObject):
	__slots__ = ['plugin', 'name', 'statusmsg', 'eta', 'done', 'total', 'owner', 'type', 'download']

	def __init__(self, plugin=None, name=None, statusmsg=None, eta=None, done=None, total=None, owner=None, type=None, download=None):
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
	__slots__ = ['speed', 'linkstotal', 'linksqueue', 'sizetotal', 'sizequeue', 'notifications', 'paused', 'download', 'reconnect', 'quota']

	def __init__(self, speed=None, linkstotal=None, linksqueue=None, sizetotal=None, sizequeue=None, notifications=None, paused=None, download=None, reconnect=None, quota=None):
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
	__slots__ = ['uid', 'name', 'email', 'role', 'permission', 'folder', 'traffic', 'dllimit', 'dlquota', 'hddquota', 'user', 'templateName']

	def __init__(self, uid=None, name=None, email=None, role=None, permission=None, folder=None, traffic=None, dllimit=None, dlquota=None, hddquota=None, user=None, templateName=None):
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
		self.templateName = templateName

class UserDoesNotExist(ExceptionObject):
	__slots__ = ['user']

	def __init__(self, user=None):
		self.user = user

class Iface(object):
	def addLinks(self, pid, links):
		pass
	def addLocalFile(self, pid, name, path):
		pass
	def addPackage(self, name, links, password):
		pass
	def addPackageChild(self, name, links, password, root, paused):
		pass
	def addPackageP(self, name, links, password, paused):
		pass
	def addUser(self, username, password):
		pass
	def checkContainer(self, filename, data):
		pass
	def checkHTML(self, html, url):
		pass
	def checkLinks(self, links):
		pass
	def createAccount(self, plugin, loginname, password):
		pass
	def createPackage(self, name, folder, root, password, site, comment, paused):
		pass
	def deleteConfig(self, plugin):
		pass
	def deleteFiles(self, fids):
		pass
	def deletePackages(self, pids):
		pass
	def findFiles(self, pattern):
		pass
	def findPackages(self, tags):
		pass
	def freeSpace(self):
		pass
	def generateDownloadLink(self, fid, timeout):
		pass
	def generatePackages(self, links):
		pass
	def getAccountInfo(self, aid, plugin, refresh):
		pass
	def getAccountTypes(self):
		pass
	def getAccounts(self):
		pass
	def getAddonHandler(self):
		pass
	def getAllFiles(self):
		pass
	def getAllInfo(self):
		pass
	def getAllUserData(self):
		pass
	def getAvailablePlugins(self):
		pass
	def getConfig(self):
		pass
	def getConfigValue(self, section, option):
		pass
	def getCoreConfig(self):
		pass
	def getFileInfo(self, fid):
		pass
	def getFileTree(self, pid, full):
		pass
	def getFilteredFileTree(self, pid, full, state):
		pass
	def getFilteredFiles(self, state):
		pass
	def getInfoByPlugin(self, plugin):
		pass
	def getInteractionTasks(self, mode):
		pass
	def getLog(self, offset):
		pass
	def getPackageContent(self, pid):
		pass
	def getPackageInfo(self, pid):
		pass
	def getPluginConfig(self):
		pass
	def getProgressInfo(self):
		pass
	def getQuota(self):
		pass
	def getServerVersion(self):
		pass
	def getStatusInfo(self):
		pass
	def getUserData(self):
		pass
	def getWSAddress(self):
		pass
	def invokeAddon(self, plugin, func, func_args):
		pass
	def invokeAddonHandler(self, plugin, func, pid_or_fid):
		pass
	def isInteractionWaiting(self, mode):
		pass
	def loadConfig(self, name):
		pass
	def login(self, username, password):
		pass
	def moveFiles(self, fids, pid):
		pass
	def movePackage(self, pid, root):
		pass
	def orderFiles(self, fids, pid, position):
		pass
	def orderPackage(self, pids, position):
		pass
	def parseLinks(self, links):
		pass
	def pauseServer(self):
		pass
	def pollResults(self, rid):
		pass
	def quit(self):
		pass
	def recheckPackage(self, pid):
		pass
	def removeAccount(self, account):
		pass
	def removeFiles(self, fids):
		pass
	def removePackages(self, pids):
		pass
	def removeUser(self, uid):
		pass
	def restart(self):
		pass
	def restartFailed(self):
		pass
	def restartFile(self, fid):
		pass
	def restartPackage(self, pid):
		pass
	def saveConfig(self, config):
		pass
	def searchSuggestions(self, pattern):
		pass
	def setConfigValue(self, section, option, value):
		pass
	def setInteractionResult(self, iid, result):
		pass
	def setPackagePaused(self, pid, paused):
		pass
	def setPassword(self, username, old_password, new_password):
		pass
	def stopAllDownloads(self):
		pass
	def stopDownloads(self, fids):
		pass
	def togglePause(self):
		pass
	def toggleReconnect(self):
		pass
	def unpauseServer(self):
		pass
	def updateAccount(self, aid, plugin, loginname, password):
		pass
	def updateAccountInfo(self, account):
		pass
	def updatePackage(self, pack):
		pass
	def updateUserData(self, data):
		pass
	def uploadContainer(self, filename, data):
		pass
