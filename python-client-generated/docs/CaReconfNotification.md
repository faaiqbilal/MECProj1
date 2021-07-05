# CaReconfNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associate_id** | [**list[AssociateId]**](AssociateId.md) | 0 to N identifiers to associate the event for a specific UE or flow. | [optional] 
**carrier_aggregation_meas_info** | [**list[CaReconfNotificationCarrierAggregationMeasInfo]**](CaReconfNotificationCarrierAggregationMeasInfo.md) | This parameter can be repeated to contain information of all the carriers assign for Carrier Aggregation up to M. | [optional] 
**ecgi** | [**Ecgi**](Ecgi.md) |  | 
**notification_type** | **str** | Shall be set to \&quot;CaReConfNotification\&quot;. | 
**secondary_cell_add** | [**list[CaReconfNotificationSecondaryCellAdd]**](CaReconfNotificationSecondaryCellAdd.md) |  | [optional] 
**secondary_cell_remove** | [**list[CaReconfNotificationSecondaryCellAdd]**](CaReconfNotificationSecondaryCellAdd.md) |  | [optional] 
**time_stamp** | [**TimeStamp**](TimeStamp.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

