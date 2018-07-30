# -*- coding: utf-8 -*-

from knitter.webelement import WebElement
from selenium.webdriver.common.by import By
from knitter import log
import time

def UnfoldHierarchyNode(name):
    if HierarchyTree.HierarchyTreeAction().VerifyUnfold(name):
        HierarchyTree.HierarchyTreeAction().Unfold_Node(name)

class CustomerCodeLabel(WebElement):
    (by, value) = (By.XPATH, "//div[text()='客户编码']")

class AddHierarchyButton(WebElement):
    (by, value) = (By.XPATH, "//span[@class='fa btn-icon icon-add']")

class SearchHierarchyButton(WebElement):
    (by, value) = (By.XPATH, "//span[@class='fa icon-search']")


#add
class SearchInfo():
    class BaseLabel(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-asset-searchPage-content-title']")

    class SearchScopeButton(WebElement):
        (by, value) = (By.XPATH, "//div[text()='默认在整个客户下搜索，点击选择具体搜索范围']")

    class SearchScope(WebElement):
        (by, value) = (By.XPATH, "//div[@class='operation-prompt']")

    class SearchScopeItem(WebElement):
        (by, value) = (By.XPATH, "//div[@class='node-content-text' and text()='#@Name']")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def Click(self, name):
            self.value = self.value.replace('#@Name', name)
            super(SearchInfo.SearchScopeItem, self).Click()

    class PanelRadio(WebElement):
        (by, value) = (By.XPATH, "//label[text()='配电柜']")

        class PanelName(WebElement):
            (by, value) = (By.XPATH, "//label[text()='配电柜名称']/../input")

        class PanelType(WebElement):
            (by, value) = (By.XPATH, "//label[text()='配电柜型号']/../input")

        class PanelManufacturer(WebElement):
            (by, value) = (By.XPATH, "//label[text()='生产厂商']/../input")

        class StartDate(WebElement):
            (by, value) = (By.XPATH, "//label[text()='起始日期']/../input")

        class EndDate(WebElement):
            (by, value) = (By.XPATH, "//label[text()='结束日期']/../input")

    class DeviceRadio(WebElement):
        (by, value) = (By.XPATH, "//label[text()='设备']")

        class DeviceName(WebElement):
            (by, value) = (By.XPATH, "//label[text()='设备名称']/../input")

        class DeviceType(WebElement):
            (by, value) = (By.XPATH, "//label[text()='设备类型']/../input")

        class DeviceModel(WebElement):
            (by, value) = (By.XPATH, "//label[text()='设备型号']/../input")

        class TrippingUnitType(WebElement):
            (by, value) = (By.XPATH, "//label[text()='脱扣单元类型']/../input")

        class DeviceManufacturer(WebElement):
            (by, value) = (By.XPATH, "//label[text()='设备厂家']/../input")

    class SearchButton(WebElement):
        (by, value) = (By.XPATH, "//span[text()='搜索']")

    class ClearSearchConditionButton(WebElement):
        (by, value) = (By.XPATH, "//div[text()='清空搜索条件']")

    class ResultCount(WebElement):
        (by, value) = (By.XPATH, "//div[@class='body']/table[@class='table fixed-table']/tbody/tr")

    class SearchResultLabel(WebElement):
        (by, value) = (By.XPATH, "//div[text()='清空搜索条件']")

class Orgnization(WebElement):
    (by, value) = (By.XPATH, "//div[text()='组织']")

class Site(WebElement):
    (by, value) = (By.XPATH, "//div[text()='园区']")

class Building(WebElement):
    (by, value) = (By.XPATH, "//div[text()='建筑']")

class PanelRoom(WebElement):
    (by, value) = (By.XPATH, "//div[text()='配电室']")

class DataRoom(WebElement):
    (by, value) = (By.XPATH, "//div[text()='数据机房']")

class InverterRoom(WebElement):
    (by, value) = (By.XPATH, "//div[text()='变频室']")

class System(WebElement):
    (by, value) = (By.XPATH, "//div[text()='系统']")

class PanelBox(WebElement):
    (by, value) = (By.XPATH, "//div[text()='配电柜']")

class DataCabinet(WebElement):
    (by, value) = (By.XPATH, "//div[text()='数据机柜']")

class TransformerCabinet(WebElement):
    (by, value) = (By.XPATH, "//div[text()='变压器柜']")

class SystemDevices(WebElement):
    (by, value) = (By.XPATH, "//div[text()='系统装置']")

class Device(WebElement):
    (by, value) = (By.XPATH, "//div[text()='设备']")

class EditButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='form-bottom-bar-btn']//span[text()='编辑']")

class DeleteButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='form-bottom-bar-btn']//span[text()='删除']")

class CancelButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='form-bottom-bar-btn']//span[text()='取消']")

class OrgnizationInfo():
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

class SaveHierarchyButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='form-bottom-bar-btn']//span[text()='保存']")

class SiteInfo():
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class FloorArea(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//input")
        index = 1
    class BuildingArea(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//input")
        index = 2

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class BuildingInfo():
    class Name(WebElement):
        (by, value) = (By.XPATH, "//label[text()='建筑名称']/../input")

    class BuildingArea(WebElement):
        (by, value) = (By.XPATH, "//label[text()='建筑面积 (m²)']/../input")

    class Completedate(WebElement):
        (by, value) = (By.XPATH, "//div[@class='datepicker-text']/input")

    class BuildingPosition(WebElement):
        (by, value) = (By.XPATH, "//label[text()='地理位置']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class PanelRoomInfo:
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class PanelPosition(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//input")
        index = 1

    class TransformerCapacity(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//input")
        index = 2

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class DataRoomInfo(WebElement):
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class PanelPosition(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//input")
        index = 1

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='改造日期']/../input")

    class BelongtoDepartment(WebElement):
        (by, value) = (By.XPATH, "//label[text()='所属部门']/../input")

    class Manager(WebElement):
        (by, value) = (By.XPATH, "//label[text()='负责人']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class InverterRoomInfo(WebElement):
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class PanelPosition(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//input")
        index = 1

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='改造日期']/../input")

    class BelongtoDepartment(WebElement):
        (by, value) = (By.XPATH, "//label[text()='所属部门']/../input")

    class Manager(WebElement):
        (by, value) = (By.XPATH, "//label[text()='负责人']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class SystemInfo(WebElement):
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='改造日期']/../input")

    class BelongtoDepartment(WebElement):
        (by, value) = (By.XPATH, "//label[text()='所属部门']/../input")

    class Manager(WebElement):
        (by, value) = (By.XPATH, "//label[text()='负责人']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class PanelBoxInfo:
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class AssetNumber(WebElement):
        (by, value) = (By.XPATH, "//label[text()='资产编号']/../input")

    class PanelType(WebElement):
        (by, value) = (By.XPATH, "//label[text()='型号']/../input")

    class PanelProduct(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产厂商']/../input")

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='改造日期']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class DataCabinetInfo(WebElement):
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class AssetNumber(WebElement):
        (by, value) = (By.XPATH, "//label[text()='资产编号']/../input")

    class Type(WebElement):
        (by, value) = (By.XPATH, "//label[text()='型号']/../input")

    class Manufacturer(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产厂商']/../input")

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='改造日期']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class TransformerCabinetInfo(WebElement):
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class AssetNumber(WebElement):
        (by, value) = (By.XPATH, "//label[text()='资产编号']/../input")

    class Type(WebElement):
        (by, value) = (By.XPATH, "//label[text()='型号']/../input")

    class Manufacturer(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产厂商']/../input")

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH,"//label[text()='生产日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH,"//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH,"//label[text()='改造日期']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class SystemDevicesInfo(WebElement):
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class AssetNumber(WebElement):
        (by, value) = (By.XPATH, "//label[text()='资产编号']/../input")

    class Type(WebElement):
        (by, value) = (By.XPATH, "//label[text()='型号']/../input")

    class Manufacturer(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产厂商']/../input")

    class InstallCompany(WebElement):
        (by, value) = (By.XPATH, "//label[text()='安装公司']/../input")

    class InstallDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='生产日期']/../input")

    class RunDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='运行日期']/../input")

    class ModificationDate(WebElement):
        (by, value) = (By.XPATH, "//label[text()='改造日期']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

class DeviceInfo:
    class Name(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField-focus']//input")

    class AssetNumber(WebElement):
        (by, value) = (By.XPATH, "//label[text()='资产编号']/../input")

    class DeviceDescription(WebElement):
        (by, value) = (By.XPATH, "//label[text()='设备描述']/../input")

    class DeviceProduct(WebElement):
        (by, value) = (By.XPATH, "//label[text()='设备厂家']/../input")

    class DeviceCost(WebElement):
        (by, value) = (By.XPATH, "//label[text()='设备成本']/../input")

    class DeviceLife(WebElement):
        (by, value) = (By.XPATH, "//label[text()='设备寿命']/../input")

    class Image(WebElement):
        (by, value) = (By.ID, 'pop_image_upload_button')

    # 设备总称
    class DeviceClass(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableDropDownMenu-ddm']/div/div/div")
        index = 1

    # 设备总称为：设备与驱动
    class DeviceClassName(WebElement):
        (by, value) = (By.XPATH, "//html/body/div[3]/div/div/div/div[12]/span/div/div")

class HierarchyTree:
    class HierarchyTreeItem(WebElement):
        (by, value) = (By.XPATH, "//div[@class='node-content-text']//span[text()='@#Name']")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def Click_Node(self, name):
            self.value = self.value.replace('@#Name', name)
            super(HierarchyTree.HierarchyTreeItem, self).Click()
            time.sleep(1)

        def VerifyExistence(self, name, TrueOrFalse=True):
            self.value = self.value.replace('@#Name', name)
            super(HierarchyTree.HierarchyTreeItem, self).VerifyExistence(TrueOrFalse)

    class HierarchyTreeAction(WebElement):
        (by, value) = (By.XPATH, "//div[@class='content' and @title='@#Name']//em[@class='fa icon-hierarchy-fold']")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def Unfold_Node(self, name):
            self.value = self.value.replace('@#Name', name)
            super(HierarchyTree.HierarchyTreeAction, self).Click()
            time.sleep(1)

        def VerifyUnfold(self, name):
            self.value = self.value.replace('@#Name', name)
            return super(HierarchyTree.HierarchyTreeAction, self).IsExist()

    class CopyButton(WebElement):
        (by, value) = (By.XPATH,"//div[@class='content' and @title='@#Name']/div/div[@class='action node-content-icon icon-copy']")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def Click(self, name):
            self.value = self.value.replace('@#Name', name)
            super(HierarchyTree.CopyButton, self).Click()

class DeleteConfirmDialog():
    class DeleteButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']//span[text()='删除']")

    class QuitButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']//span[text()='放弃']")

class ForbiddenDeleteMessageBox():
    class CloseButton(WebElement):
        (by, value) = (By.XPATH, "//h3[contains(text(),'无法删除')]/../div/div[@class='dialog-close-icon icon-close']")

class SceneLogDialog():
    class LogContent(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-viewableTextField']//textarea")
        index = 1

    class LogAttachment(WebElement):
        (by, value) = (By.ID, "pop-attachment-add")

    class SaveButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']/button[1]")

    class QuitButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']/button[2]")

    class AttachmentDeleteButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='attachment-delete-overlay'][index]")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def Click(self, index):
            self.value = self.value.replace('index', index)
            super(SceneLogDialog.AttachmentDeleteButton, self).Click()

class SceneLogItems:
    class LogItems(WebElement):
        (by, value) = (By.XPATH, "//div[@class='logs-panel-item']")

    class LogEditButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='logs-panel-item-buttons']//a[text()='编辑']")

    class LogDeleteButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='logs-panel-item-buttons']//a[text()='删除']")

    class LogText(WebElement):
        (by, value) = (By.XPATH, "//div[@class='logs-panel-item-text']//span[text()='该日志已经被编辑']")

    class LogAttachment(WebElement):
         (by, value) = (By.XPATH, "//div[@class='logs-panel-item-picture-panel']")

class HierarchyFold(WebElement):
    (by, value) = (By.XPATH, "//em[@class='fa icon-hierarchy-fold']")

class AddSceneLogButton(WebElement):
    (by, value) = (By.XPATH, "//div[@class='form-bottom-bar-btn']//span[text()='添加现场日志']")

class Administrators(WebElement):
    class AddAdministratorsButton(WebElement):
        (by, value) = (By.XPATH, "//h3[text()='维护负责人（选填）']/../span[text()='添加']")

    class DeleteAdministratorsButton(WebElement):
        (by, value) = (By.XPATH, "//a[text()='删除']")

    class EditAdministrators(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-admin-container']//span[@class='pop-admin-name']")

    class AdministratorsName(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-admin-window']//div[@class='pop-viewableTextField-focus']/input")

    class AdministratorsTitle(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-admin-window']//label[text()='职位']/../input")

    class AdministratorsTelephone(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-admin-window']//label[text()='手机']/../input")

    class AdministratorsEmail(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-admin-window']//label[text()='电子邮箱']/../input")

    class AddButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']//span[text()='添加']/..")

    class CancelButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']//span[text()='放弃']/..")

    class DoneButton(WebElement):
        (by, value) = (By.XPATH, "//div[@class='dialog-actions']//span[text()='完成']/..")

    class AdministratorsContents(WebElement):
        (by, value) = (By.XPATH, "//div[@class='pop-admin-container']//span[text()='@#Name']")

        def __init__(self):
            by = WebElement.by
            value = WebElement.value

        def VerifyExistence(self, name, trueORfalse):
            self.value = self.value.replace('#@Name', name)
            super(Administrators.AdministratorsContents, self).VerifyExistence(trueORfalse)
