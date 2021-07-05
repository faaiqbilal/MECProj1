# MeasRepUeNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associate_id** | [**list[AssociateId]**](AssociateId.md) | 0 to N identifiers to associate the event for a specific UE or flow. | [optional] 
**carrier_aggregation_meas_info** | [**list[MeasRepUeNotificationCarrierAggregationMeasInfo]**](MeasRepUeNotificationCarrierAggregationMeasInfo.md) | This parameter can be repeated to contain information of all the carriers assign for Carrier Aggregation up to M. | [optional] 
**ecgi** | [**Ecgi**](Ecgi.md) |  | 
**eutran_neighbour_cell_meas_info** | [**list[MeasRepUeNotificationEutranNeighbourCellMeasInfo]**](MeasRepUeNotificationEutranNeighbourCellMeasInfo.md) | This parameter can be repeated to contain information of all the neighbouring cells up to N. | [optional] 
**height_ue** | **int** | Indicates height of the UE in meters relative to the sea level as defined in ETSI TS 136.331 [i.7]. | [optional] 
**new_radio_meas_info** | [**list[MeasRepUeNotificationNewRadioMeasInfo]**](MeasRepUeNotificationNewRadioMeasInfo.md) | 5G New Radio secondary serving cells measurement information. | [optional] 
**new_radio_meas_nei_info** | [**list[MeasRepUeNotificationNewRadioMeasNeiInfo]**](MeasRepUeNotificationNewRadioMeasNeiInfo.md) | Measurement quantities concerning the 5G NR neighbours. | [optional] 
**notification_type** | **str** | Shall be set to \&quot;MeasRepUeNotification\&quot;. | 
**rsrp** | **int** | Reference Signal Received Power as defined in ETSI TS 136 214 [i.5]. | 
**rsrp_ex** | **int** | Extended Reference Signal Received Power, with value mapping defined in ETSI TS 136 133 [i.16]. | [optional] 
**rsrq** | **int** | Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5]. | 
**rsrq_ex** | **int** | Extended Reference Signal Received Quality, with value mapping defined in ETSI TS 136 133 [i.16]. | [optional] 
**sinr** | **int** | Reference Signal \&quot;Signal to Interference plus Noise Ratio\&quot;, with value mapping defined in ETSI TS 136 133 [i.16]. | [optional] 
**time_stamp** | [**TimeStamp**](TimeStamp.md) |  | [optional] 
**trigger** | [**Trigger**](Trigger.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

