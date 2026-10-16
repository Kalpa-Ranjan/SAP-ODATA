



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJZXB4I5%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T121119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIA1I%2BgMvRcqLIyqZQiNU8K35emsGjn2ffCLoxp8Ow%2FjEAiEAwNJg4Wvx4WGnusoygmXQ2zaknKBx%2BhpMl4XMFic0xasqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMUhPGBHmDwlKa1iCyrcAzCtwknI2ZSBL6rZItKP1nUo3Nkte99gOBIxQyyFxeXhMh%2BBhAEnOcviz6Udj%2F17p0BlyqnQecEtawcnxiZiotk7U2kv%2FML7T01eNU1dajK79IApjrhDE9Ongs32wABMLX3Of6oOk6EuovJ2vmw7c86C%2FrfC8Fv3zAuq60qP4J%2BkSrwS%2FdhVdzTkLH%2FbbhcIbcwwDUffaK9MOWwaY6uvnKkvhnO7%2F9amV56sHxVCkXSdEZDNBWpAXPn136lrBASSXEZtguFAaP%2FwANcejLZJ4A1Zs4VnR5%2BUI%2FjpsxsNIxH1gBhaz%2BXTjHHngg5LwikLNQXkTGrUnd2v7Vfa8V9Zt6PYKdstiNtA005u9m6wtX9tfI5vbV%2FYWj57ijLgSqtBE2FWo9IuWOn%2B2mAj%2BSVrZE%2Fcv6kGezyXgeYC5RhvyHsj1yrSJaeKhurAlz4bhp%2Fj%2FF0Jq5oHOW3b6zbdLGJjO%2FVGTSWr3dOW3imawQSmQB0Lna015TgLvpDcIK%2B1pHKBXQBtTU%2FYgMfbm4LD9mnMQDQ66onhLk8NMsbNiZcG00lOkFjaBMgNWTsX1xPw7Al7zKdW9h97sIoFHAE7EpGj7o1ZNv6MsUa%2B3%2BMvRXpLQ9RFswKIR5kVP3QtJygDMJClyNYGOqUBogxxmz%2FAwcayg2mebI8UygMHqOsgMMbBbL6B1iEmwsOu9%2B4JsmP%2BTvRpN0%2BNpVQR4rT91zGBv3pnxeinfGwkvjHkgAnem9JzFyL2STh7NA2HT%2BmEDYkZoV1PClRItTrpNEtFcMfY4lyLzldiI32xn30CzuwmBGcIiFIHIMXDuk8M%2FOf57N9IsA%2Fv7UHDvMR3FgYBMzX7JA8viNtgPnq%2Bll9teyd%2B&X-Amz-Signature=23c7d7463e0e64df4725db12e0a594db42a992d86437b16827834d7d2da8605c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJZXB4I5%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T121119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIA1I%2BgMvRcqLIyqZQiNU8K35emsGjn2ffCLoxp8Ow%2FjEAiEAwNJg4Wvx4WGnusoygmXQ2zaknKBx%2BhpMl4XMFic0xasqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMUhPGBHmDwlKa1iCyrcAzCtwknI2ZSBL6rZItKP1nUo3Nkte99gOBIxQyyFxeXhMh%2BBhAEnOcviz6Udj%2F17p0BlyqnQecEtawcnxiZiotk7U2kv%2FML7T01eNU1dajK79IApjrhDE9Ongs32wABMLX3Of6oOk6EuovJ2vmw7c86C%2FrfC8Fv3zAuq60qP4J%2BkSrwS%2FdhVdzTkLH%2FbbhcIbcwwDUffaK9MOWwaY6uvnKkvhnO7%2F9amV56sHxVCkXSdEZDNBWpAXPn136lrBASSXEZtguFAaP%2FwANcejLZJ4A1Zs4VnR5%2BUI%2FjpsxsNIxH1gBhaz%2BXTjHHngg5LwikLNQXkTGrUnd2v7Vfa8V9Zt6PYKdstiNtA005u9m6wtX9tfI5vbV%2FYWj57ijLgSqtBE2FWo9IuWOn%2B2mAj%2BSVrZE%2Fcv6kGezyXgeYC5RhvyHsj1yrSJaeKhurAlz4bhp%2Fj%2FF0Jq5oHOW3b6zbdLGJjO%2FVGTSWr3dOW3imawQSmQB0Lna015TgLvpDcIK%2B1pHKBXQBtTU%2FYgMfbm4LD9mnMQDQ66onhLk8NMsbNiZcG00lOkFjaBMgNWTsX1xPw7Al7zKdW9h97sIoFHAE7EpGj7o1ZNv6MsUa%2B3%2BMvRXpLQ9RFswKIR5kVP3QtJygDMJClyNYGOqUBogxxmz%2FAwcayg2mebI8UygMHqOsgMMbBbL6B1iEmwsOu9%2B4JsmP%2BTvRpN0%2BNpVQR4rT91zGBv3pnxeinfGwkvjHkgAnem9JzFyL2STh7NA2HT%2BmEDYkZoV1PClRItTrpNEtFcMfY4lyLzldiI32xn30CzuwmBGcIiFIHIMXDuk8M%2FOf57N9IsA%2Fv7UHDvMR3FgYBMzX7JA8viNtgPnq%2Bll9teyd%2B&X-Amz-Signature=b614dbd0924c87b9b8d18b804e32e8fccf755249f6e8f5c451264698dabd5257&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







