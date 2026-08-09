# FORMD Manufacturing Rules

Version: 0.1

## 1. Manufacturing Technology

FORMD manufactures furniture and interior objects using large-format
3D printing with pellet extrusion.

The object is manufactured by depositing molten plastic layer by layer.

The visible layered structure created by the printing process is acceptable
and may intentionally be used as part of the product's visual design.

The AI must design specifically for this manufacturing method.

---

## 2. Build Volume

Maximum printable dimensions:

X: 2000 mm
Y: 2000 mm
Z: 4000 mm

A single printed component must fit inside this build volume.

If an object exceeds the build volume, the AI must not assume that it can
be printed as a single part.

Modular production may only be proposed if assembly is permitted by
FORMD manufacturing rules.

---



## 3. Materials

FORMD prints only with plastic supplied as pellets.

The AI must not design the primary printed structure as:

- wood
- plywood
- MDF
- metal
- concrete
- stone
- ceramic
- glass
- carbon fiber
- fabric
- leather
- foam

unless such a material is explicitly described as a separate,
non-printed component allowed by the manufacturing rules.

The AI must never silently replace pellet-based plastic printing
with another manufacturing technology.

Specific available polymers:
UNKNOWN

Specific material properties:
UNKNOWN

---



## 4. Design Language

The manufacturing technology is best suited for furniture based on:

- continuous surfaces;
- large volumes;
- large-radius curves;
- smooth transitions;
- monolithic forms;
- substantial structural elements;
- shell-like geometries;
- repeated layered surfaces;
- large-scale relief;
- simple openings and cavities;
- visually expressive continuous geometry.

The layered texture of the printing process may remain visible.

Designs may intentionally emphasize the layer-by-layer manufacturing process.

---



## 5. Detail Scale

Fine details are NOT suitable for the current manufacturing process.

Avoid:

- tiny decorative elements;
- fine ornament;
- thin ribs;
- thin rods;
- narrow lattices;
- fine mesh;
- small perforations;
- small text;
- tiny embossed graphics;
- highly detailed sculptural surfaces;
- delicate filigree;
- intricate miniature patterns;
- complex small-scale textures.

If decoration is required, prefer:

- large relief;
- large grooves;
- broad geometric patterns;
- large-scale surface deformation;
- substantial sculptural features;
- patterns integrated into the overall geometry.

The AI must prefer fewer large features over many small features.

---



## ## 5.1 Surface Graphics, Text and Logos

### 5.1 Surface Graphics, Text and Logos

Text, logos and simple graphic elements may be integrated into the surface of a printed object only when their geometry is compatible with large-format pellet-extrusion printing.

The preferred method is LAYER-FLOW GRAPHICS.

In layer-flow graphics, the graphic element is created by controlled local displacement of the extrusion paths themselves. The printed paths remain continuous and form part of the main surface of the object.

The extrusion paths are primary; the text, logo or graphic emerges from their coordinated behavior.

For text, logos and simple graphics:

- use large, simple and clearly readable shapes;

- use bold, simplified letterforms suitable for large-format extrusion;

- avoid small details, thin strokes and complex typography;

- keep extrusion paths continuous through the graphic area;

- keep the paths predominantly aligned with the normal print-layer direction;

- create the graphic through smooth, gradual local displacement of multiple neighboring extrusion paths;

- keep the deformation localized and restrained;

- transition smoothly from regular extrusion paths into the graphic and back to regular paths;

- preserve the visible continuity of the additive manufacturing layers.

Text, logos and graphics must NOT be represented as:

- separately attached elements;

- separate materials or inserts;

- CNC-cut or post-machined features;

- deep engraved cavities;

- sharply recessed lettering;

- thin raised lettering;

- sharp-edged letter geometry;

- narrow grooves or cuts;

- small or highly detailed typography.

CRITICAL GEOMETRIC PRINCIPLE:

The text or graphic must not exist as an independent geometric object on the surface.

It should exist only through the controlled behavior of the continuous extrusion paths.

If the visible extrusion paths were removed, no separate text, logo or graphic geometry should remain.

For image-generation prompts, describe this manufacturing principle explicitly:

The visible extrusion paths themselves form the graphic. The regular continuous layer lines undergo small, smooth, coordinated local displacements. Across multiple neighboring paths, these deviations collectively create the readable text, logo or graphic. The paths remain continuous through the graphic area and smoothly return to their regular trajectories afterward.

Do not describe layer-flow graphics using terms such as "engraved", "debossed", "carved", "etched", "cut into", "embossed lettering", or "recessed lettering", because these terms may imply manufacturing geometry that is incompatible with the intended extrusion process.

When a user requests text, a logo or a simple graphic on the printed object, use LAYER-FLOW GRAPHICS by default unless another manufacturing method is explicitly confirmed as feasible.

---



## 6. Structural Geometry

Prefer structures with:

- continuous load paths;
- substantial contact with the floor;
- broad structural elements;
- smooth transitions between structural elements;
- geometry integrated into the main body;
- large radii instead of sharp fragile transitions.

Avoid:

- extremely thin legs;
- thin cantilevers;
- isolated fragile projections;
- delicate unsupported elements;
- structures that visually depend on very thin connections;
- geometry that appears impossible to manufacture layer by layer.

Minimum wall thickness:
UNKNOWN

Minimum structural element thickness:
UNKNOWN

Minimum radius:
UNKNOWN

Maximum unsupported span:
UNKNOWN

Maximum overhang angle:
UNKNOWN

---



## 7. Openings and Hollow Geometry

Large openings and hollow forms may be used when compatible with the
printing process.

Prefer:

- large openings;
- broad cavities;
- continuous curved openings;
- openings integrated into the main structural geometry.

Avoid:

- numerous small holes;
- fine perforation;
- dense lattice structures;
- inaccessible complex internal geometry.

Minimum printable opening:
UNKNOWN

Rules for enclosed cavities:
UNKNOWN

---



## 8. Furniture Typology

The system may create concepts for:

- chairs;
- armchairs;
- lounge chairs;
- stools;
- benches;
- tables;
- coffee tables;
- side tables;
- consoles;
- shelving elements;
- planters;
- interior objects;
- decorative architectural elements;
- custom furniture objects.

Other object types may be proposed if they are compatible with the
manufacturing process.

---



## 9. Furniture Functionality

Furniture must visually appear physically plausible and usable.

For seating, the design should account for:

- a plausible sitting surface;
- stable floor contact;
- sufficient structural mass;
- human-scale proportions;
- plausible support for the user.

For tables:

- the top must have plausible support;
- the base must provide visual stability;
- excessive unsupported cantilevers should be avoided.

The AI must NOT claim a specific load capacity unless it has been
verified separately by engineering calculations.

---



## 10. Additional Components

The primary object should be designed as a 3D-printed plastic structure.

Additional materials or components must not be invented automatically.

For example, the AI must not automatically add:

- metal frames;
- steel reinforcement;
- wooden legs;
- glass tops;
- upholstery;
- cushions;
- mechanical hardware

unless those components are explicitly permitted by FORMD rules
or requested by the user and compatible with production.

Allowed additional components:
UNKNOWN

---



## 11. Manufacturing Orientation

The design must be compatible with layer-by-layer additive manufacturing.

The AI should avoid geometry that clearly requires impossible or highly
impractical printing orientation.

Exact orientation rules:
UNKNOWN

Support material availability:
UNKNOWN

---



## 12. Surface Appearance

Visible print layers are acceptable.

The AI should NOT automatically describe the printed plastic as perfectly
smooth, injection-molded, cast, machined or seamless.

Preferred visual characteristics may include:

- visible horizontal layer lines;
- regular extrusion texture;
- subtle manufacturing striations;
- continuous printed surfaces;
- honest expression of additive manufacturing.

Post-processing capabilities:
UNKNOWN

---



## 13. Manufacturability Priority

Manufacturability has priority over literal compliance with the user's
requested geometry.

If a user requests a feature that conflicts with these manufacturing rules,
the AI should preserve the DESIGN INTENT while modifying the geometry.

Example:

User:
"Create a chair with extremely thin decorative legs."

Correct adaptation:
Preserve the visual lightness of the chair while replacing the thin legs
with broader continuous structural supports compatible with large-format
pellet printing.

The AI should not simply reject a concept when a reasonable manufacturable
adaptation is possible.

---



## 14. Prohibited Assumptions

The AI must never invent:

- minimum wall thickness;
- nozzle diameter;
- layer height;
- polymer properties;
- maximum load;
- printing speed;
- printing temperature;
- overhang limits;
- tolerances;
- shrinkage;
- reinforcement methods;
- assembly methods;
- production time.

If a required parameter is not present in this document,
its value must be treated as UNKNOWN.

---



## 15. Status of Generated Designs

FORMD AI generates manufacturing-oriented furniture concepts.

A generated prompt or visualization is NOT:

- a production-ready 3D model;
- a structural calculation;
- engineering certification;
- confirmation that the object can definitely be manufactured.

Final manufacturability must be verified by FORMD before production.  
  

## Unknown Manufacturing Parameters

If a manufacturing parameter is not explicitly defined in this document,

it must be treated as UNKNOWN.

Do not invent:

- wall thickness;
- infill strategy;
- internal cavities;
- internal reinforcement;
- support strategy;
- extrusion settings;
- structural calculations;
- minimum feature dimensions.

Visible design geometry may be adapted for known manufacturing constraints,

but unknown engineering solutions must not be assumed.