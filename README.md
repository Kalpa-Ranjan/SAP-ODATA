



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XFV4WZO%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T064235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyI3n2QDlC1h5TVslAXL1UuMBtBoodxnBaqLcabvHChQIgXluQad9MsOU4JEpEO0njZpao1oVkXhVfp%2FoHN9d4sx0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPo673ppBZljRgr1LircAyx1IerXOGhVKubLJK7cQKlUnOEad5HoMgvw6bUNMyfI4TdJz6PVtKp6kb0cQQ0JwUP4LfJc0k%2BTB61wZyw89%2BbzT72dF4sDs6uaqhXd1SYmbI6PkmiJs2K1rgOOzf2gLmhUnsmzLBFRL0qKbOxbPn8kuqOO5%2F75sRTXYSamfcRfNXPXhMwEXbN7ZuW%2BRXFyUED8Vc5TRh0TOUdPNRaZt54t%2BBWyvlPbTEP1nB88PevADoXYCxmhspDEM4u%2B9ZFv8coKPxQdA7%2BxN%2FlzW8uMSvhEjm5uLr7x2Azbu8uH8vEJH%2FYc0iHPqx5%2BzHi3lua8rB9PamYcWGxzmjgL4D%2BqQ79sdW4%2BVhuABbbDv8XuifwHrqv5etCDzsEI%2BKz9EnRSVGlFWmY2Bd5quOyyyrbZxXaftcfSbW1ANNgogiJNHA6kkbIguWNwE0SIiFoQnas612TmRh0BvL9HOStOcUcNSdD4Y87vRmeUmT3aS2M9QONf3Nwm9WFC0lUzs12d8bi5pRJFj%2B%2Fg%2Bx7MoBis3ML4ovMCREiPwr1zk2jei6DWg%2BL5MB826weTi3vpCiDgjFTp8%2BISDOrO2FzHKQGrXfLIM4ffDwtyC3cXBPdJwAJsfDJ2903rgIcUgOCYjSdiMKmQ%2B8sGOqUBEFbmHgBrprG4FfiusJvI7CBQoE%2B09ME%2F5vhFVxVIQEp5k7c%2B%2FL5wE%2BO45gS1eTDrFt6LQ7xpfCc0tQrv%2FE%2FmO8HhH%2BzwTsT%2FBZTKVJ4UVfKzzKfPMXyFh2ESKaJTX9ug51hEkI0qtJ%2FV7toYx4iM8kHz4%2FTaEMgGiUt%2FCKgiaaXe5Zh9OO5Xkaeu%2FjPprwskjUcfw4fOVW6Ys75gUu777rF0webZ&X-Amz-Signature=b3333d24a7f67ca6005c5f5c43ece2dd7631732d7bc7eef58cb37d2034703751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XFV4WZO%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T064236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyI3n2QDlC1h5TVslAXL1UuMBtBoodxnBaqLcabvHChQIgXluQad9MsOU4JEpEO0njZpao1oVkXhVfp%2FoHN9d4sx0qiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPo673ppBZljRgr1LircAyx1IerXOGhVKubLJK7cQKlUnOEad5HoMgvw6bUNMyfI4TdJz6PVtKp6kb0cQQ0JwUP4LfJc0k%2BTB61wZyw89%2BbzT72dF4sDs6uaqhXd1SYmbI6PkmiJs2K1rgOOzf2gLmhUnsmzLBFRL0qKbOxbPn8kuqOO5%2F75sRTXYSamfcRfNXPXhMwEXbN7ZuW%2BRXFyUED8Vc5TRh0TOUdPNRaZt54t%2BBWyvlPbTEP1nB88PevADoXYCxmhspDEM4u%2B9ZFv8coKPxQdA7%2BxN%2FlzW8uMSvhEjm5uLr7x2Azbu8uH8vEJH%2FYc0iHPqx5%2BzHi3lua8rB9PamYcWGxzmjgL4D%2BqQ79sdW4%2BVhuABbbDv8XuifwHrqv5etCDzsEI%2BKz9EnRSVGlFWmY2Bd5quOyyyrbZxXaftcfSbW1ANNgogiJNHA6kkbIguWNwE0SIiFoQnas612TmRh0BvL9HOStOcUcNSdD4Y87vRmeUmT3aS2M9QONf3Nwm9WFC0lUzs12d8bi5pRJFj%2B%2Fg%2Bx7MoBis3ML4ovMCREiPwr1zk2jei6DWg%2BL5MB826weTi3vpCiDgjFTp8%2BISDOrO2FzHKQGrXfLIM4ffDwtyC3cXBPdJwAJsfDJ2903rgIcUgOCYjSdiMKmQ%2B8sGOqUBEFbmHgBrprG4FfiusJvI7CBQoE%2B09ME%2F5vhFVxVIQEp5k7c%2B%2FL5wE%2BO45gS1eTDrFt6LQ7xpfCc0tQrv%2FE%2FmO8HhH%2BzwTsT%2FBZTKVJ4UVfKzzKfPMXyFh2ESKaJTX9ug51hEkI0qtJ%2FV7toYx4iM8kHz4%2FTaEMgGiUt%2FCKgiaaXe5Zh9OO5Xkaeu%2FjPprwskjUcfw4fOVW6Ys75gUu777rF0webZ&X-Amz-Signature=f2aed0a940a85783afa0b216551a4442cf8ee426cd6b3798dcf3aea035d1adee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







