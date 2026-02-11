



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MQUPTGM%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T065540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC38sAETM%2BzvXt5Ggy%2Bp0%2BvuOFlvz0%2F8%2FGKTWChNhmLtAIgbUTN5ilUcGi9VmDUdJYjCONbca2TwgYkyA2%2Fwif%2Fvx4qiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtofyM%2F7%2BygwZHj%2FyrcA71AyDX54ycC3RydC50WLYx3pOF571JTQp9UZZ6hTPP20T8DA9ghs0UEtiXA1Tq3OBCWSE3grWlvCOzGcUQI2dit6OKYzdtK%2FXqeTfRFouqw1b%2BGpIifc92xA1tddP9TqnOsASq%2FExZcnPi66Wy4oxpygL2lPoelFoWc8B8SZey2WedqnwaSHk3lpqiBbZ%2BvdVzD1bnB%2BSGOLr%2FPx4wWnQI2xlalGpsZ4Xysso4td91PAbUime9moKvqlVCdUAXsFu%2BBNuHnTjjzA92RFc4hf1RSrn5suEczJV3LITB6U%2BNfj9w%2BtKAQY5P0rR0DSnVcxYSvWeg8uaugoYXw8rhxE9tWKB8tHIWNMdKRbVI1VZy6wpf2IED7MBpsEkmXlgKdByoziC2L0ynJH1%2FTMQ5nO4oLCHPwOpI%2Fwo4cRDy4uBUJeT1D6v7eNatnhXUxFYJLG6zb2VZgbxAY9rIW5VDZRb5fF7JHKENO%2BXU0BXLtAtqtCKtc6aQnAZdzgS0g%2BzhpboTBBegDsT%2FwSPNV1b47THQpg6OX5F%2Fp1IrvtYKi66Cr%2BoWjtANCTAhTG2aq8EFsh3qisaQSfVWcptVGhr64DVvhYikXDYxV6Ps9METpNca8jjEpwztZvTyFKKPnMKi9sMwGOqUBB8zp2GzhHoYZfqXIh5g6lPMEohgxBNwTXjk1gxZ1NE3ZKhFx4GZaCHpmVNyC%2BPIPpmtaBWCDquHXoEgyad9mV9ZSvliEf6jiZ%2BR7uDZvK88Rm1n1MLTJpENiPhbprgoAuI2h0CzQl6dnZk6DPskKPuoThUll4EQmV3Se57NT0BQle%2FF8w%2FmUWzTLsIYZuzGqaTqJ6%2FDg70bwJKOryKet1qI8xbLf&X-Amz-Signature=661667756ad396a826daebfe785e721f3182147781eab457b5d84190808b3b8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MQUPTGM%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T065540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC38sAETM%2BzvXt5Ggy%2Bp0%2BvuOFlvz0%2F8%2FGKTWChNhmLtAIgbUTN5ilUcGi9VmDUdJYjCONbca2TwgYkyA2%2Fwif%2Fvx4qiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtofyM%2F7%2BygwZHj%2FyrcA71AyDX54ycC3RydC50WLYx3pOF571JTQp9UZZ6hTPP20T8DA9ghs0UEtiXA1Tq3OBCWSE3grWlvCOzGcUQI2dit6OKYzdtK%2FXqeTfRFouqw1b%2BGpIifc92xA1tddP9TqnOsASq%2FExZcnPi66Wy4oxpygL2lPoelFoWc8B8SZey2WedqnwaSHk3lpqiBbZ%2BvdVzD1bnB%2BSGOLr%2FPx4wWnQI2xlalGpsZ4Xysso4td91PAbUime9moKvqlVCdUAXsFu%2BBNuHnTjjzA92RFc4hf1RSrn5suEczJV3LITB6U%2BNfj9w%2BtKAQY5P0rR0DSnVcxYSvWeg8uaugoYXw8rhxE9tWKB8tHIWNMdKRbVI1VZy6wpf2IED7MBpsEkmXlgKdByoziC2L0ynJH1%2FTMQ5nO4oLCHPwOpI%2Fwo4cRDy4uBUJeT1D6v7eNatnhXUxFYJLG6zb2VZgbxAY9rIW5VDZRb5fF7JHKENO%2BXU0BXLtAtqtCKtc6aQnAZdzgS0g%2BzhpboTBBegDsT%2FwSPNV1b47THQpg6OX5F%2Fp1IrvtYKi66Cr%2BoWjtANCTAhTG2aq8EFsh3qisaQSfVWcptVGhr64DVvhYikXDYxV6Ps9METpNca8jjEpwztZvTyFKKPnMKi9sMwGOqUBB8zp2GzhHoYZfqXIh5g6lPMEohgxBNwTXjk1gxZ1NE3ZKhFx4GZaCHpmVNyC%2BPIPpmtaBWCDquHXoEgyad9mV9ZSvliEf6jiZ%2BR7uDZvK88Rm1n1MLTJpENiPhbprgoAuI2h0CzQl6dnZk6DPskKPuoThUll4EQmV3Se57NT0BQle%2FF8w%2FmUWzTLsIYZuzGqaTqJ6%2FDg70bwJKOryKet1qI8xbLf&X-Amz-Signature=5c65b2ff928b7c53eff1a08058ccfb55df6613c2a51e67fc2c10be5a6393d849&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







