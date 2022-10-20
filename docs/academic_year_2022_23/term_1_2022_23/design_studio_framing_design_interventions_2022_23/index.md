Design Studio Term 1 2022-23
========
# Framing Design Interventions

<style>
#hcg-slider-1 .hcg-slide-container {
	width: auto;
	height: auto;
}
.hcg-slider {
	text-align: center;
	font-family: Arial, Helvetica, sans-serif;
}
.hcg-slide-container {
	max-width: 100%;
	display: inline-block;
	position: relative;
}
.hcg-slides {
	display: none;
	overflow: hidden;
	justify-content: center;
	align-items: center;
	border-radius: 5px;
	border: solid 1px #a0a0a0;
}
.hcg-slides img {
	max-width: 100%;
	max-height: 100%;
	display: inline-block;
}
#hcg-slide-prev, #hcg-slide-next {
	cursor: pointer;
	position: absolute;
	top: 50%;
	width: auto;
	padding: 16px;
	margin-top: -22px;
	color: #fff;
	font-weight: bold;
	font-size: 18px;
	transition: 0.6s ease;
	border-radius: 0 3px 3px 0;
	text-decoration: none;
	text-shadow: 1px 1px 5px #686868;
}
#hcg-slide-next {
	right: 0;
	border-radius: 3px 0 0 3px;
}
#hcg-slide-prev {
	left: 0;
	border-radius: 0 3px 3px 0;
}
#hcg-slide-prev:hover, #hcg-slide-next:hover {
	background-color: #000c;
}
.hcg-slide-dot-control {
	margin-top: 10px;
	text-align: center;
}
.hcg-slide-dot {
	cursor: pointer;
	height: 13px;
	width: 13px;
	margin: 0 2px;
	background-color: #bbb;
	border-radius: 50%;
	display: inline-block;
}
.hcg-slide-dot.dot-active {
	background-color: #717171;
}
.hcg-slide-number {
	color: #ffffff;
	font-size: 12px;
	padding: 4px 7px;
	position: absolute;
	border-radius: 5px;
	top: 5px;
	left: 5px;
	background-color: rgba(255,255,255,0.30);
}
/************CSS Animation***********/

.animated {
	animation-name: fadeIn;
	animation-duration: 1s;
}
@keyframes fadeIn {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}
.fadeIn {
	animation-name: fadeIn;
}


</style>

<script>
(() => {
//If you want to add more images, add the link name and URL image URL in the array list below.
	const images_list = [
{
    "url": "https://html-generator.com/uploads/images/2022/10/20/08993YQ7USGP1P9.jpeg",
    "alt": "",
    "name": "08993YQ7USGP1P9.jpeg",
    "link": ""
},
{
    "url": "https://html-generator.com/uploads/images/2022/10/20/39386B035MY_SCQ.jpeg",
    "alt": "",
    "name": "39386B035MY_SCQ.jpeg",
    "link": ""
},
{
    "url": "https://html-generator.com/uploads/images/2022/10/20/11626QDPKVUAV4P.jpeg",
    "alt": "",
    "name": "11626QDPKVUAV4P.jpeg",
    "link": ""
},
{
    "url": "https://html-generator.com/uploads/images/2022/10/20/759985L0ASE9IRP.jpeg",
    "alt": "",
    "name": "759985L0ASE9IRP.jpeg",
    "link": ""
},
{
    "url": "https://html-generator.com/uploads/images/2022/10/20/07326QMXSVPJW6I.jpg",
    "alt": "",
    "name": "07326QMXSVPJW6I.jpg",
    "link": ""
}
	];

// generated by https://www.html-code-generator.com/html/image-slideshow-generator
	let slider_id = document.querySelector("#hcg-slider-1");

	// append all images
	let dots_div = "";
	let images_div = "";
	for (let i = 0; i < images_list.length; i++) {
		// if no link without href="" tag
		let href = (images_list[i].link == "" ? "":' href="'+images_list[i].link+'"');
		images_div += '<a'+href+' class="hcg-slides animated"'+(i === 0 ? ' style="display:flex"':'')+'>'+
						'<span class="hcg-slide-number">'+(i+1)+'/'+images_list.length+'</span>'+
						'<img src="'+images_list[i].url+'" alt="'+images_list[i].name+'">'+
					 '</a>';
		dots_div += '<a href="#" class="hcg-slide-dot'+(i === 0 ? ' dot-active':'')+'" data-id="'+i+'"></a>';
	}
	slider_id.querySelector(".hcg-slider-body").innerHTML = images_div;
	slider_id.querySelector(".hcg-slide-dot-control").innerHTML = dots_div;

	let slide_index = 0;

	const images = slider_id.querySelectorAll(".hcg-slides");
	const dots = slider_id.querySelectorAll(".hcg-slide-dot");
	const prev_button = slider_id.querySelector("#hcg-slide-prev");
	const next_button = slider_id.querySelector("#hcg-slide-next");

	const showSlides = () => {
		if (slide_index > images.length-1) {
			slide_index = 0;
		}
		if (slide_index < 0) {
			slide_index = images.length-1;
		}
		for (let i = 0; i < images.length; i++) {
			images[i].style.display = "none";
			dots[i].classList.remove("dot-active");
			if (i == slide_index) {
				images[i].style.display = "flex";
				dots[i].classList.add("dot-active");
			}
		}
	}

	prev_button.addEventListener("click", event => {
		event.preventDefault();
		slide_index--;
		showSlides();
	}, false);

	next_button.addEventListener("click", event => {
		event.preventDefault();
		slide_index++;
		showSlides();
	}, false);

	const dot_click = event => {
		event.preventDefault();
		slide_index = event.target.dataset.id;
		showSlides();
	}

	for (let i = 0; i < dots.length; i++) {
		dots[i].addEventListener("click", dot_click, false);
	}
})();
</script>

<div id="hcg-slider-1" class="hcg-slider">
	<div class="hcg-slide-container">
	<div class="hcg-slider-body">
		<a class="hcg-slides animated" style="display:flex">
			<span class="hcg-slide-number">1/5</span>
			<img src="https://html-generator.com/uploads/images/2022/10/20/08993YQ7USGP1P9.jpeg" alt="08993YQ7USGP1P9.jpeg">
			<span class="hcg-slide-text">08993YQ7USGP1P9.jpeg</span>
		</a>
	</div>
	<a href="#" id="hcg-slide-prev">❮</a>
	<a href="#" id="hcg-slide-next">❯</a>
</div>
<div class="hcg-slide-dot-control"></div>
</div>

## Track
Application

## Faculty
Oscar Tomico, Mariana Quintero, Tomas Diez, Jonathan Minchin, Tomas Vivanco  

## Syllabus

MDEF Research, Design and Development studios aim to take research areas of interest and initial project ideas into an advanced concretion point, and execution plan. The studio structure in three terms could be understood as follows:

**TERM 1 Research**: Understanding what it means to design for emergent futures. Analyzing the past and finding weak signals. References, state of the art. Identifying areas of interest. Experimenting from the first-person perspective.

**TERM 2 Design**: Forming the present through interventions in the real world. Building the foundations of your design space, forming strategic partnerships. Applying knowledge into practice through iterative prototyping. Testing ideas and prototypes in the real world.

**TERM 3 Development**: Refining interventions and identifying desirable futures. Establishing roadmaps for the construction of emergent narratives.. Communicating and disseminating your project through speculative design.

The first term Design Studio aims to create a solid ground for the students to start developing their projects. Weekly activities will be set to interlink results from the courses like their mappings, cartographies, experiments, 1st person design activities, prototypes, with their personal development plan. In order to propose an area of intervention at the end of the trimester. The Design Studio activities will consist of presentations, group activities, short exercises and personal coaching. The specific goals are the following:

To develop a critical position in the student’s design practice.
Define possible areas of intervention, based on the Atlas of the Week Signals.
Prototype an alpha version of the design space and iterate.
To build personal and collective repositories of resources.

## When  
**Every Monday**

## Schedule

### 03/10 Bootcamp Kick off - Pick your fight(s).

**Goals**: Integrate personal and professional interests.

**Activity 1**: Pick your fight(s). Make a poster of your interests.

**Activity 2**: Create your vision (pushing your fight further) and Identity (skills, knowledge, attitude), collaboration plan.

**Deliverable 1**: Post the poster on your website.

**Deliverable 2**: Document your vision, identity, collaboration plan and reflect on your personal development.

### 10/10 Roles of Prototyping in 1PP Research through Design

**Goals**: To learn about the different roles of prototyping in design research. Being resilient and resourceful as a professional. Learn about 1PP RTD iterative design interventions methodology.

**Activity 1**: From the different roles that prototypes play in design research, reflect which ones you have used in the past and which ones you could include in your practice.

**Activity 2**: Reflect on your own RtD toolbox based on your vision and identity. Select the main roles of prototyping and other design activities that you want to use based on the context you are in (onion mapping).

**Deliverable**: 1 Post on your website with your new extended workspace

### 17/10 Design Studio Reviews


### 24/10 Areas of interventions in a Multiscalar Design Space. Collaborative design spaces and interventions .

**Goals**: To explore and develop forms of aggregative documentation, building collective design spaces.

**Activity**: Develop a collective framework to document explorations using the existing digital platforms, build digital maps of resources and opportunities in the design studio.

**Deliverable**: A collaborative map of projects, resources, news, and opportunities for interventions … that can populate your physical working space and a plan on how to share relevant information between all of you on-line.

**Task**: Carry out different pilot design interventions to understand in an embodied and situated way your design space.

### 31/10 Design Studio Reviews


### 07/11 Video Journaling and Other Forms of 1PP Documentation and communication.

**Objectives**: Learn new ways of documenting and communicating. Integrate documentation and communication as part of your daily activities.

**Activity**: Reflect on how you are documenting and communicating the courses and the project. Present the successes and points of improvement.

**Assignment**: Document the course “Measuring the World + Almost Useful Machines”.

**Deliverable 1**: A reflection on how you are documenting and communicating your work.

**Deliverable 2**: A video which can include multiple ways of video journaling (interviews, personal reflections, activities, ...).

### 14/11 Design Studio Reviews


### 21/11 Collective design intervention: a collective design action with humans and/or non-humans + ELISAVA & Fab Lab Research Presentations

**Goals**: Situate your collective explorations in context to frame to update your collective design space.

**Activity**: Plan your collective design intervention and map the actors and infrastructure you want to involve.

**Task**: Execute your first collective design intervention for the next design studio.

**Deliverable**: Document the collective design intervention, analyze it and reflect on the findings.



### 28/11 Design Studio Reviews (group)


### 12/12  Design Dialogues Preparation

**Goals**: Create a collective and individual building up plan for the Design Dialogues exhibition.

**Activity**: Group dynamic to create themes and groups of projects for the exhibition.

**Deliverable**: Planning of the exhibition, space allocation and special needs.

**Task**: Work on the design dialogues deliverables.



###  22/12  Design Dialogues (Proposed date TBC)

**Objectives**: to present collective areas of intervention and to present the first experiments at a personal and collective level, and in an immediate context. To produce the first group exhibition of the master’s projects.

**Deliverables**: A series of prototypes presented in a collective design space and a personal video of no more than 3 minutes (answering the question what is your updated fight),

**Deliverables for after the holidays**: 5 high resolution images of the highlights of your Design Studio work during the term, a high resolution image of your personal and Collective design space and the first chapters of your Thesis Draft which represent each one of the deliverables developed during the term:

**Chapter 0**: What is your fight?. Vision and Identity. Personal development and Collaboration Plan.

**Chapter 1**: Research through Design Toolbox.

**Chapter 2**: Framing a collective Design Space based on AoWS, Multiscalar Design Space and State of the Art. Personally  reflect on your area of interest and an area of intervention.

**Chapter 3**: First interventions (Experiments, Pilots and first collective intervention): Description and results.

### Evaluation
**These are the points we are going to look at for Term 1:**

  ● Relevance of the project in relation to the weak signals

  ● Framing of the opportunity through the Collective Design Space

  ● Involvement of the community through the collective interventions

## Grading Method

33% of the evaluation will be the Design Studio faculties’ combined grade, 33% will be the average grade your peers give you, and 33% will be the completion of your first Thesis draft.



## Tomas Diez

![](../../../assets/images/faculty_photos/tomas_diez.jpg)

Tomas Diez is a Venezuelan Urbanist specialized in digital fabrication and its implications on the future cities and society. He is the co-founder of Fab Lab Barcelona, leads the Fab City Research Laboratory, and is a founding partner of the Fab City Global Initiative. He is the director of the Master in Design for Emergent Futures at the Institute for Advanced Architecture of Catalonia (IAAC) in Barcelona, where he is faculty in urban design and digital fabrication. Tomas is co-founder of other initiatives such as Smart Citizen (open source tools for citizen engagement), Fab City (locally productive, globally-connected cities), Fablabs.io (the listing of fab labs in the world), and StudioP52 (art and design space in Barcelona).

<!--[Email](tomasdiez@iaac.net) -->

[Personal Website](http://tomasdiez.com/)

[Twitter Account](@tomasdiez)

[Facebook](tomasdiez77)


## Oscar Tomico

![](../../../assets/images/faculty_photos/oscar_tomico.jpg)

Oscar Tomico holds an MSc degree in Industrial Engineering from Polytechnic University of Catalonia (Spain) and a PhD from the same institution, awarded in 2007 with Cum Laude. During his research into Innovation Processes in Product Design, he investigated subjective experience-gathering techniques based on constructivist psychology. After finishing his PhD he worked as a consultant for Telefonica R&D (Barcelona). Tomico joined Eindhoven University of Technology (TU/e) in 2007 as Assistant Professor. He has been a guest researcher and lecturer at AUT Creative technologies (New Zealand), at TaiwanTech (Taiwan), Swedish School of Textiles (Sweden), Institute of Advanced Architecture (Spain), University of Tsukuba, Aalto (Finland) to name a few. During his sabbatical in 2015, he worked as a consultant for the functional textiles department at EURECAT (Spain). He recently (2017) became the head of the Industrial Design Bachelor’s degree program at ELISAVA University School of Design and Engineering of Barcelona.

<!--[Email](otomico@elisava.net)-->

[Personal Website](https://www.elisava.net/en/teaching-staff)

Twitter Account @otomico

## Mariana Quintero

![](../../../assets/images/faculty_photos/mariana_quintero.jpg)

Multimedia developer, interaction designer & researcher, Mariana Quintero works and develops her practice at the intersection where digital fabrication technologies, digital literacy, and information and computation ethics & aesthetics meet, contributing to projects that investigate how digital information and technologies translate, represent, and mediate knowledge about the world. She is currently a faculty member and part of the strategic team at the Masters in Design for Emergent Futures at IAAC | Fab Lab Barcelona

<!--[Email](mariana.quintero@iaac.net)-->

[Personal Website](https://mqvlm.github.io/)