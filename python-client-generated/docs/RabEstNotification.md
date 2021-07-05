# RabEstNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associate_id** | [**list[AssociateId]**](AssociateId.md) | 0 to N identifiers to bind the event for a specific UE or flow.  | [optional] 
**ecgi** | [**Ecgi**](Ecgi.md) |  | 
**erab_id** | **int** | The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3]. | 
**erab_qos_parameters** | [**RabEstNotificationErabQosParameters**](RabEstNotificationErabQosParameters.md) |  | [optional] 
**notification_type** | **str** | Shall be set to \&quot;RabEstNotification\&quot;. | 
**temp_ue_id** | [**RabEstNotificationTempUeId**](RabEstNotificationTempUeId.md) |  | [optional] 
**time_stamp** | [**TimeStamp**](TimeStamp.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

