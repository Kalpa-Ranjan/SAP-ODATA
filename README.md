



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM2PVIKI%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T123835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIF26ncr5kCGB5YLyHutSqwyjdvztL8JZ6mFuqA63SmHUAiEA6iI1ZgtLpcLq3nmn%2F6klr9hijqHoeYkMquiDgEVik%2FYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDWhI%2BRvEIiHfpLU6CrcA2dgXMOvL05q0ZVjl2BcXoHzzms3I%2B5rrxQUnKS0XgQat608iiP2%2Bp8%2FmjHcsKaODLAfzufTN%2BUHI2mK9sKNB7uBagtrweiR%2FLUeAqlT9kycxc9948AF38pB3QcPSUMQcBC30d%2F03jwxykIUeOlIQER%2BZWPRLk6nL2NoxoTVaQBae8h8GIop9zFM0FujYKg0eky9Pgg46HrJMmGv1gjFAx8dZ7U0JOXQlat04HFCHr7gRJeENbf0BrLgEMfOMvnwykhQ0F9UIe0igBzt%2B1LP%2FYp3XKnVkcO6NDDuiAFwobaUGrw5zi0i9K3c%2B8DQ3bFIrR0CPEgZQkFbIJ2wKbe21XY2BlJzuL%2FV4m9t7lfZR66ptU3e307uthMwFRhiQ130ZwPxGG7NhPLhocnNXxBSMg6qcKeyDT1AMpSYA2WtJtPnvZuUN1H5qqZmWex%2B4xNA2G9MKKSVAkxJiZNNYoXNcCO5FzZ752L64C%2FjfBm61g2tL3TZyISy4fuPXa3mFiiitCt5Pf2st4GhfDS4C2vH03dlmewut9nlcbmf7d95YZMjMKmkHkNB%2BfrsrqUbi%2B3Xf6qe1rhPBZgCyX5w%2Bo8BYfBHBBhnvEbtFPARw%2BYpFYxzdHhm1uoomKle7yQTMLStyMsGOqUBA3d1l3dEU9nT0PXQhP8j8plLDqgVpglUY8CW8kq2e7q9mwsnyYAz0y9nrRMSG%2BMOxKCEVoXBilJTvwjeHV3GpVmSbERhXcIBq7f8G365%2FzBckpDwnbaPKKGVaCOYyqnoIy6yC7AnAZnJ1O4QP2s7CGcifavAiAWY2ZM1CpnUVuTTMoQhi25YN5nsYhp0DWWnSdOmNlQMIdwnKmTHMI%2BpihK2OZyF&X-Amz-Signature=1cfba2418981bed62cac120759f2d3c9a895bde4480678c6d0a05677edae5766&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM2PVIKI%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T123835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIF26ncr5kCGB5YLyHutSqwyjdvztL8JZ6mFuqA63SmHUAiEA6iI1ZgtLpcLq3nmn%2F6klr9hijqHoeYkMquiDgEVik%2FYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDWhI%2BRvEIiHfpLU6CrcA2dgXMOvL05q0ZVjl2BcXoHzzms3I%2B5rrxQUnKS0XgQat608iiP2%2Bp8%2FmjHcsKaODLAfzufTN%2BUHI2mK9sKNB7uBagtrweiR%2FLUeAqlT9kycxc9948AF38pB3QcPSUMQcBC30d%2F03jwxykIUeOlIQER%2BZWPRLk6nL2NoxoTVaQBae8h8GIop9zFM0FujYKg0eky9Pgg46HrJMmGv1gjFAx8dZ7U0JOXQlat04HFCHr7gRJeENbf0BrLgEMfOMvnwykhQ0F9UIe0igBzt%2B1LP%2FYp3XKnVkcO6NDDuiAFwobaUGrw5zi0i9K3c%2B8DQ3bFIrR0CPEgZQkFbIJ2wKbe21XY2BlJzuL%2FV4m9t7lfZR66ptU3e307uthMwFRhiQ130ZwPxGG7NhPLhocnNXxBSMg6qcKeyDT1AMpSYA2WtJtPnvZuUN1H5qqZmWex%2B4xNA2G9MKKSVAkxJiZNNYoXNcCO5FzZ752L64C%2FjfBm61g2tL3TZyISy4fuPXa3mFiiitCt5Pf2st4GhfDS4C2vH03dlmewut9nlcbmf7d95YZMjMKmkHkNB%2BfrsrqUbi%2B3Xf6qe1rhPBZgCyX5w%2Bo8BYfBHBBhnvEbtFPARw%2BYpFYxzdHhm1uoomKle7yQTMLStyMsGOqUBA3d1l3dEU9nT0PXQhP8j8plLDqgVpglUY8CW8kq2e7q9mwsnyYAz0y9nrRMSG%2BMOxKCEVoXBilJTvwjeHV3GpVmSbERhXcIBq7f8G365%2FzBckpDwnbaPKKGVaCOYyqnoIy6yC7AnAZnJ1O4QP2s7CGcifavAiAWY2ZM1CpnUVuTTMoQhi25YN5nsYhp0DWWnSdOmNlQMIdwnKmTHMI%2BpihK2OZyF&X-Amz-Signature=f265628c67320f02e296a423f36f6fb36239c4c335303aae4f561df93221592c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







