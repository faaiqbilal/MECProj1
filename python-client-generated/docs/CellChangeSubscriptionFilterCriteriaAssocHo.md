# CellChangeSubscriptionFilterCriteriaAssocHo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **str** | Unique identifier for the MEC application instance. | [optional] 
**associate_id** | [**list[AssociateId]**](AssociateId.md) | 0 to N identifiers to associate the information for a specific UE or flow. | [optional] 
**ecgi** | [**list[Ecgi]**](Ecgi.md) | E-UTRAN Cell Global Identifier. | [optional] 
**ho_status** | [**list[Enum]**](Enum.md) | In case hoStatus is not included in the subscription request, the default value 3 &#x3D; COMPLETED shall be used and included in the response: &lt;p&gt;1 &#x3D; IN_PREPARATION. &lt;p&gt;2 &#x3D; IN_EXECUTION. &lt;p&gt;3 &#x3D; COMPLETED. &lt;p&gt;4 &#x3D; REJECTED. &lt;p&gt;5 &#x3D; CANCELLED. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

