# NrMeasRepUeNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associate_id** | [**list[AssociateId]**](AssociateId.md) | 0 to N identifiers to associate the event for a specific UE or flow. | [optional] 
**eutra_neigh_cell_meas_info** | [**list[NrMeasRepUeNotificationEutraNeighCellMeasInfo]**](NrMeasRepUeNotificationEutraNeighCellMeasInfo.md) | This parameter can be repeated to contain measurement information of all the neighbouring cells up to N. It shall not be included if nrNeighCellMeasInfo is included. | [optional] 
**notification_type** | **str** | Shall be set to \&quot;NrMeasRepUeNotification\&quot;. | 
**nr_neigh_cell_meas_info** | [**list[NrMeasRepUeNotificationNrNeighCellMeasInfo]**](NrMeasRepUeNotificationNrNeighCellMeasInfo.md) | This parameter can be repeated to contain measurement information of all the neighbouring cells up to N. It shall not be included if eutraNeighCellMeasInfo is included. | [optional] 
**serv_cell_meas_info** | [**list[NrMeasRepUeNotificationServCellMeasInfo]**](NrMeasRepUeNotificationServCellMeasInfo.md) | This parameter can be repeated to contain information of all the serving cells up to N. | [optional] 
**time_stamp** | [**TimeStamp**](TimeStamp.md) |  | [optional] 
**trigger_nr** | [**TriggerNr**](TriggerNr.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

