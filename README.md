



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLDHGDHO%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T094229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1YlhAc%2FQVwPCCMon8n80sx73MLBWXAfrq7HMJUpFgUAiACtYfoPN5MdFoXdlVMxJWyu%2FfYilIgjeiJSMs1cLRIhir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMHrqEBRHori5r9P53KtwDhl3g5HMVvTV47nXQwSxUzFkmvhYvsVTbA%2FmuzAt0GhAOKXva%2F1TrbX7Xhc2DyqOilccqKzbGQERII3UhlU9kpRXM%2BGYBGFXnTtUFb1LNbvlmFQMvwV0P8aXglfzx3leJGmtptmIBjlA45M5LWVSCdFwO7pn4ix2XRWZlZeeYOTJmdFEEnB3Id%2BbhHKkNzbODunVEil6UxfvIydrBaQtr3yG57tUWCLE5yTBGf6%2FvMeJNDa%2BEHNb2FKU7Sntmw7nr3ZMNNYdXn9%2BOPobMT%2BbOjKmjJeIL1XAN%2FcWpqYuz%2BgASVreg7zrddr0132aoW1WLr1Bg9NDB6Nlf0ViW42YCxiYCgM6l%2B5QPlx9XBI%2FhlASwlngnHVlZ%2FC0v2eYzgAbnaAYPruvH7jOiq%2FrMJt6mtP7AT70qNrSUmHEY9zVuelupmK5MyXSattWpx1p%2BlJ%2BxwdNJyZZCyF9bWJq5IDotXZ8ZKK8A0S%2Bg%2FITWErCwXCMyMSB8Kaq8vHF7LtVyQAx91tWzftmoHmefvydSMTqD8beKC3tqwDFe9K9uMjfcMHVy%2F2PuuGPV9CLuL%2Bn1%2B056H%2F%2BVw01G7boypL7J76Fo10GbVnw3efmmDPjl66GIS4PH3x88HDWY2IK9JBAwnLnV0AY6pgGxD215AmzmI41a6hhctnqeoydyNcqqKSIcwtcx1caVFmk6qnA86lziP%2FoVOH6o6nn1HrJiPPNC8IMGfHlwIbZ5%2B6rY5DFpeXexe5BHHszYcYduZ%2BG8AHnHvAsX4qmMy1spXUGueW%2FydzMLcn7OPuoLLIz3ft0KMxwQ4TudzBtFIqk%2BygGsq%2BFm3kyxbuXlkrs2JUP5jS%2Fc08mwQSL4ije6EdeQszq5&X-Amz-Signature=9d64a9e846506c8766153135398d026ab9f2df44bd1409f15cbba4bf19d5dff7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLDHGDHO%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T094229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID1YlhAc%2FQVwPCCMon8n80sx73MLBWXAfrq7HMJUpFgUAiACtYfoPN5MdFoXdlVMxJWyu%2FfYilIgjeiJSMs1cLRIhir%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMHrqEBRHori5r9P53KtwDhl3g5HMVvTV47nXQwSxUzFkmvhYvsVTbA%2FmuzAt0GhAOKXva%2F1TrbX7Xhc2DyqOilccqKzbGQERII3UhlU9kpRXM%2BGYBGFXnTtUFb1LNbvlmFQMvwV0P8aXglfzx3leJGmtptmIBjlA45M5LWVSCdFwO7pn4ix2XRWZlZeeYOTJmdFEEnB3Id%2BbhHKkNzbODunVEil6UxfvIydrBaQtr3yG57tUWCLE5yTBGf6%2FvMeJNDa%2BEHNb2FKU7Sntmw7nr3ZMNNYdXn9%2BOPobMT%2BbOjKmjJeIL1XAN%2FcWpqYuz%2BgASVreg7zrddr0132aoW1WLr1Bg9NDB6Nlf0ViW42YCxiYCgM6l%2B5QPlx9XBI%2FhlASwlngnHVlZ%2FC0v2eYzgAbnaAYPruvH7jOiq%2FrMJt6mtP7AT70qNrSUmHEY9zVuelupmK5MyXSattWpx1p%2BlJ%2BxwdNJyZZCyF9bWJq5IDotXZ8ZKK8A0S%2Bg%2FITWErCwXCMyMSB8Kaq8vHF7LtVyQAx91tWzftmoHmefvydSMTqD8beKC3tqwDFe9K9uMjfcMHVy%2F2PuuGPV9CLuL%2Bn1%2B056H%2F%2BVw01G7boypL7J76Fo10GbVnw3efmmDPjl66GIS4PH3x88HDWY2IK9JBAwnLnV0AY6pgGxD215AmzmI41a6hhctnqeoydyNcqqKSIcwtcx1caVFmk6qnA86lziP%2FoVOH6o6nn1HrJiPPNC8IMGfHlwIbZ5%2B6rY5DFpeXexe5BHHszYcYduZ%2BG8AHnHvAsX4qmMy1spXUGueW%2FydzMLcn7OPuoLLIz3ft0KMxwQ4TudzBtFIqk%2BygGsq%2BFm3kyxbuXlkrs2JUP5jS%2Fc08mwQSL4ije6EdeQszq5&X-Amz-Signature=be92657169df8d44bcfd7839731232ff770c8a23fa67d8fdb49727a50578dbd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







