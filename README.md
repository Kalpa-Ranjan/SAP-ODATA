



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJGWM5U%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T121012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIDpfgJgGhRVSFCvCI8xn9Ef1trRBVMTyGg6yncGea1oIAiEAikkunn08eDxs9BgWG0ITRJbHiHxcs1TG7E%2BCPPnr%2FwgqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFBsdFgP%2FU%2B%2Fi2URwSrcAwzj6uzqC%2FewtzL53iur9T565xhBE2nq46dIINTp%2FIL%2FocAXs0FeDhiuOY7db6L8NrvA90VRmByT6kqEFMUKhVRP6wK1YSWgjKGLvmTgcMleK3uE1ZFq1oDkArPiji%2FFiXlFcHVeln4rYAZ2cUtKXhd9yTAM9RMjRshvIuAdW%2F7Q8T1OHRpGzOWJZAZVZkf6ELWoyVokQNipbqsJSwLkAQp9Y3zhOou4iDayopHtNUGBsc1uAkF42DxgFxjwuH9iBCozxpImAyFMl6WxeZoUJf7vUjNoOHw6Z4u4Pa%2Bxb0HqS9eY6erw04zXGmhlhZhr03DJbZSxcmNyJTuo%2Bqi8BG0ZGwqx%2BNI%2FQKJjranitaMUgeg3BAVsMvVLTvHHCfEMFBXWtdNG2iQ8O67NS3AhmAxY0Q7VQfi3iOw9Rs87%2B7vuFefYuyfNN%2Bf1FrfpbhpKh%2FD6KLwhOXvGj%2BYu9fDtr%2BxeyhTASgYRsYLSwwEHxmFf5nyWcxk3iPcbBaajTMHRNB%2BLNnxLaoaveei4jXIhPsMoPD3X%2BTqz4Zp1WG%2FYM1Ab5dRsmS%2FK4LgN19bnUN0QN%2BTqPLiGoFZaMJO71GeCAyEv4sqRRi%2FuZI8NGIwCnFUT2jA5%2B%2BhrYiMfeAJUMIL2mdUGOqUBAwO8BeXao33nwlp9eTnKthmLeoq9RCpxK0fgODm8nrG2uJkQzOYdVo9RX3vVGf%2BEginlwgy0yhOdKSxQQ%2BpnqElMCCQgyisThNmjM7MMAxBfS7yYE%2BdMJUesKRIVcC%2Brey1t4ZMgSntjUl6zsDAR937CYnXiteFVVD6%2FJbIUAOcnwxWeZl7NeuYQ%2FQIqFnt81NkqHW7EGDyytfmbFy7IKhUlcmy7&X-Amz-Signature=3f80fae377f75a22edc319eb095342a009c299bbc573db1bb0d188bc509ea44e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJGWM5U%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T121012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIDpfgJgGhRVSFCvCI8xn9Ef1trRBVMTyGg6yncGea1oIAiEAikkunn08eDxs9BgWG0ITRJbHiHxcs1TG7E%2BCPPnr%2FwgqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFBsdFgP%2FU%2B%2Fi2URwSrcAwzj6uzqC%2FewtzL53iur9T565xhBE2nq46dIINTp%2FIL%2FocAXs0FeDhiuOY7db6L8NrvA90VRmByT6kqEFMUKhVRP6wK1YSWgjKGLvmTgcMleK3uE1ZFq1oDkArPiji%2FFiXlFcHVeln4rYAZ2cUtKXhd9yTAM9RMjRshvIuAdW%2F7Q8T1OHRpGzOWJZAZVZkf6ELWoyVokQNipbqsJSwLkAQp9Y3zhOou4iDayopHtNUGBsc1uAkF42DxgFxjwuH9iBCozxpImAyFMl6WxeZoUJf7vUjNoOHw6Z4u4Pa%2Bxb0HqS9eY6erw04zXGmhlhZhr03DJbZSxcmNyJTuo%2Bqi8BG0ZGwqx%2BNI%2FQKJjranitaMUgeg3BAVsMvVLTvHHCfEMFBXWtdNG2iQ8O67NS3AhmAxY0Q7VQfi3iOw9Rs87%2B7vuFefYuyfNN%2Bf1FrfpbhpKh%2FD6KLwhOXvGj%2BYu9fDtr%2BxeyhTASgYRsYLSwwEHxmFf5nyWcxk3iPcbBaajTMHRNB%2BLNnxLaoaveei4jXIhPsMoPD3X%2BTqz4Zp1WG%2FYM1Ab5dRsmS%2FK4LgN19bnUN0QN%2BTqPLiGoFZaMJO71GeCAyEv4sqRRi%2FuZI8NGIwCnFUT2jA5%2B%2BhrYiMfeAJUMIL2mdUGOqUBAwO8BeXao33nwlp9eTnKthmLeoq9RCpxK0fgODm8nrG2uJkQzOYdVo9RX3vVGf%2BEginlwgy0yhOdKSxQQ%2BpnqElMCCQgyisThNmjM7MMAxBfS7yYE%2BdMJUesKRIVcC%2Brey1t4ZMgSntjUl6zsDAR937CYnXiteFVVD6%2FJbIUAOcnwxWeZl7NeuYQ%2FQIqFnt81NkqHW7EGDyytfmbFy7IKhUlcmy7&X-Amz-Signature=c9d8849caa93d72aa0cb6d75afb09e7c395fceac4f7553e538c5411912bd31cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







