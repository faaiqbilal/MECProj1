# CellChangeNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associate_id** | [**list[AssociateId]**](AssociateId.md) | 0 to N identifiers to associate the event for a specific UE or flow. | [optional] 
**ho_status** | **int** | Indicate the status of the UE handover procedure. Values are defined as following: &lt;p&gt;1 &#x3D; IN_PREPARATION. &lt;p&gt;2 &#x3D; IN_EXECUTION. &lt;p&gt;3 &#x3D; COMPLETED. &lt;p&gt;4 &#x3D; REJECTED. &lt;p&gt;5 &#x3D; CANCELLED. | 
**notification_type** | **str** | Shall be set to \&quot;CellChangeNotification\&quot;. | 
**src_ecgi** | [**Ecgi**](Ecgi.md) |  | 
**temp_ue_id** | [**CellChangeNotificationTempUeId**](CellChangeNotificationTempUeId.md) |  | [optional] 
**time_stamp** | [**TimeStamp**](TimeStamp.md) |  | [optional] 
**trg_ecgi** | [**list[Ecgi]**](Ecgi.md) | E-UTRAN Cell Global Identifier of the target cell. NOTE: Cardinality N is valid only in case of statuses IN_PREPARATION, REJECTED and CANCELLED. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

