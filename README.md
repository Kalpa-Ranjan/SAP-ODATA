



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UPRTHIP%2F20261116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261116T061230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDo%2FG8PoAxR9qVoutl8h7hC%2BmykeGxx2LqBrDNi3ycePwIgAmgKXY2ykDTi8aoZK3%2Fycsuu7nxGP6tYbq0tztodFxUqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIkd6d1sziLi1gRHircAxHXiiebY6SSPQcp9v85qgezb3RkjnSiKxIihYJC1NKaK2eMWkx%2F00OIOdHo7nePhiHCzy3Hl9v7J56%2BULAHoFBWqYVreNJ9Pk%2FgrFc7l2lxb9ESkSNzjgjUeJZVEHpznWtTuRB2HWfPthf4eZbAINcC9VMXLqCYe%2BQx2Udqd0q5nhCHVvCTzTH8iznBLXJKQ1k71UTq%2FU2DXry2MInSX3YJvf8KCK4B3ey6NIZPT6qMg2UEicG6%2FgHubDBnbyfOkzTF1pkSeVC5lfUWi10jPbyG9WS1nB6mwN42mjXoX3dJaOJmIyFImyscIAKFq0VRXUIMJqUZzYz%2BTM1M6qHpsX6oKC8mjiTJ171ym5rm7x%2F1axTMUMF0f4XWhbSPCFY5dn5Wq6tQM5SARIp1ieh6jbvuNa1M92NunQWRpx%2BU3Sb4iKVzCVbtB1nz0dxTpE3ZttvX9gjoV0Ul6pKIrjpgkQvf9%2B9V7LtX3ufc%2FKhJ3XyyPFu53j%2FJvos1KUmsbYHoj%2FA0jZnf6B8KJGgImojjW7l1jatlAhyZJH3uc7k6mxcP1IR4EZ3144EeMVmXooh%2B8hd8hPga16mzPtncIglB5XDCRYhSoK3VRRqXWfrIFyB2TKl3%2FVW61%2FFozfYwML%2B66tcGOqUBj2ovDDSK3xPSBZki1Bp%2BQGva5gPxB1z%2FLko%2BEwkSgyPKfFkSpzEFr%2B6mY6iblS3iOAbRRHscGqLSyBKlU4MFX56hKwjMKoW3jMrm1J64B6H%2FJslXBE6s1OwYY49Fv5N69pr9Ons6qNSHDBu2F95FosRn4XSdYaskZQKmO8l78rN%2FCrdam3nOe8ShwNS2X2zIFkrzvqkPYpfy%2B06zCgjCW3jYfDgR&X-Amz-Signature=6676f7a4165884b02571b2e207848a84047042b2ec317060ca73819c6215dff4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UPRTHIP%2F20261116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261116T061230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDo%2FG8PoAxR9qVoutl8h7hC%2BmykeGxx2LqBrDNi3ycePwIgAmgKXY2ykDTi8aoZK3%2Fycsuu7nxGP6tYbq0tztodFxUqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIkd6d1sziLi1gRHircAxHXiiebY6SSPQcp9v85qgezb3RkjnSiKxIihYJC1NKaK2eMWkx%2F00OIOdHo7nePhiHCzy3Hl9v7J56%2BULAHoFBWqYVreNJ9Pk%2FgrFc7l2lxb9ESkSNzjgjUeJZVEHpznWtTuRB2HWfPthf4eZbAINcC9VMXLqCYe%2BQx2Udqd0q5nhCHVvCTzTH8iznBLXJKQ1k71UTq%2FU2DXry2MInSX3YJvf8KCK4B3ey6NIZPT6qMg2UEicG6%2FgHubDBnbyfOkzTF1pkSeVC5lfUWi10jPbyG9WS1nB6mwN42mjXoX3dJaOJmIyFImyscIAKFq0VRXUIMJqUZzYz%2BTM1M6qHpsX6oKC8mjiTJ171ym5rm7x%2F1axTMUMF0f4XWhbSPCFY5dn5Wq6tQM5SARIp1ieh6jbvuNa1M92NunQWRpx%2BU3Sb4iKVzCVbtB1nz0dxTpE3ZttvX9gjoV0Ul6pKIrjpgkQvf9%2B9V7LtX3ufc%2FKhJ3XyyPFu53j%2FJvos1KUmsbYHoj%2FA0jZnf6B8KJGgImojjW7l1jatlAhyZJH3uc7k6mxcP1IR4EZ3144EeMVmXooh%2B8hd8hPga16mzPtncIglB5XDCRYhSoK3VRRqXWfrIFyB2TKl3%2FVW61%2FFozfYwML%2B66tcGOqUBj2ovDDSK3xPSBZki1Bp%2BQGva5gPxB1z%2FLko%2BEwkSgyPKfFkSpzEFr%2B6mY6iblS3iOAbRRHscGqLSyBKlU4MFX56hKwjMKoW3jMrm1J64B6H%2FJslXBE6s1OwYY49Fv5N69pr9Ons6qNSHDBu2F95FosRn4XSdYaskZQKmO8l78rN%2FCrdam3nOe8ShwNS2X2zIFkrzvqkPYpfy%2B06zCgjCW3jYfDgR&X-Amz-Signature=5221c8e6cc134eebb02435554405b8c175af86bd30d10a7e566eb7ae9ef7694b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







