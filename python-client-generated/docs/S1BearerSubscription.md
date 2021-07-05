# S1BearerSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s1_bearer_subscription_criteria** | [**S1BearerSubscriptionS1BearerSubscriptionCriteria**](S1BearerSubscriptionS1BearerSubscriptionCriteria.md) |  | 
**links** | [**CaReconfSubscriptionLinks**](CaReconfSubscriptionLinks.md) |  | [optional] 
**callback_reference** | **str** | URI selected by the service consumer, to receive notifications on the subscribed RNIS information. This shall be included in the request and response. | 
**event_type** | [**list[Enum]**](Enum.md) | Description of the subscribed event. The event is included both in the request and in the response. \\nFor the eventType, the following values are currently defined: &lt;p&gt;0 &#x3D; RESERVED. &lt;p&gt;1 &#x3D; S1_BEARER_ESTABLISH. &lt;p&gt;2 &#x3D; S1_BEARER_MODIFY. &lt;p&gt;3 &#x3D; S1_BEARER_RELEASE. | 
**expiry_deadline** | [**TimeStamp**](TimeStamp.md) |  | [optional] 
**subscription_type** | **str** | Shall be set to \&quot;S1BearerSubscription\&quot;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

