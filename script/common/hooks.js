import { DarkHeresyActor } from "./actor.js";
import { DarkHeresyItem } from "./item.js";
import { AcolyteSheet } from "../sheet/acolyte.js";
import { NpcSheet } from "../sheet/npc.js";
import { WeaponSheet } from "../sheet/weapon.js";
import { AmmunitionSheet } from "../sheet/ammunition.js";
import { WeaponModificationSheet } from "../sheet/weapon-modification.js";
import { ArmourSheet } from "../sheet/armour.js";
import { ForceFieldSheet } from "../sheet/force-field.js";
import { CyberneticSheet } from "../sheet/cybernetic.js";
import { DrugSheet } from "../sheet/drug.js";
import { GearSheet } from "../sheet/gear.js";
import { ToolSheet } from "../sheet/tool.js";
import { CriticalInjurySheet } from "../sheet/critical-injury.js";
import { MalignancySheet } from "../sheet/malignancy.js";
import { MentalDisorderSheet } from "../sheet/mental-disorder.js";
import { MutationSheet } from "../sheet/mutation.js";
import { PsychicPowerSheet } from "../sheet/psychic-power.js";
import { TalentSheet } from "../sheet/talent.js";
import { SpecialAbilitySheet } from "../sheet/special-ability.js";
import { TraitSheet } from "../sheet/trait.js";
import { initializeHandlebars } from "./handlebars.js";
import { migrateWorld } from "./migration.js";

Hooks.once("init", () => {
    CONFIG.Combat.initiative = { formula: "@initiative.base + @initiative.bonus", decimals: 0 };
    CONFIG.Actor.entityClass = DarkHeresyActor;
    CONFIG.Item.entityClass = DarkHeresyItem;
    CONFIG.fontFamilies.push("Caslon Antique");
    Actors.unregisterSheet("core", ActorSheet);
    Actors.registerSheet("dark-eye-5", AcolyteSheet, { types: ["acolyte"], makeDefault: true });
    Actors.registerSheet("dark-eye-5", NpcSheet, { types: ["npc"], makeDefault: true });
    Items.unregisterSheet("core", ItemSheet);
    Items.registerSheet("dark-eye-5", WeaponSheet, { types: ["weapon"], makeDefault: true });
    Items.registerSheet("dark-eye-5", AmmunitionSheet, { types: ["ammunition"], makeDefault: true });
    Items.registerSheet("dark-eye-5", WeaponModificationSheet, { types: ["weaponModification"], makeDefault: true });
    Items.registerSheet("dark-eye-5", ArmourSheet, { types: ["armour"], makeDefault: true });
    Items.registerSheet("dark-eye-5", ForceFieldSheet, { types: ["forceField"], makeDefault: true });
    Items.registerSheet("dark-eye-5", CyberneticSheet, { types: ["cybernetic"], makeDefault: true });
    Items.registerSheet("dark-eye-5", DrugSheet, { types: ["drug"], makeDefault: true });
    Items.registerSheet("dark-eye-5", GearSheet, { types: ["gear"], makeDefault: true });
    Items.registerSheet("dark-eye-5", ToolSheet, { types: ["tool"], makeDefault: true });
    Items.registerSheet("dark-eye-5", CriticalInjurySheet, { types: ["criticalInjury"], makeDefault: true });
    Items.registerSheet("dark-eye-5", MalignancySheet, { types: ["malignancy"], makeDefault: true });
    Items.registerSheet("dark-eye-5", MentalDisorderSheet, { types: ["mentalDisorder"], makeDefault: true });
    Items.registerSheet("dark-eye-5", MutationSheet, { types: ["mutation"], makeDefault: true });
    Items.registerSheet("dark-eye-5", PsychicPowerSheet, { types: ["psychicPower"], makeDefault: true });
    Items.registerSheet("dark-eye-5", TalentSheet, { types: ["talent"], makeDefault: true });
    Items.registerSheet("dark-eye-5", SpecialAbilitySheet, { types: ["specialAbility"], makeDefault: true });
    Items.registerSheet("dark-eye-5", TraitSheet, { types: ["trait"], makeDefault: true });
    initializeHandlebars();
    game.settings.register("dark-eye-5", "worldSchemaVersion", {
        name: "World Version",
        hint: "Used to automatically upgrade worlds data when the system is upgraded.",
        scope: "world",
        config: true,
        default: 0,
        type: Number,
    });
});

Hooks.once("ready", () => {
    migrateWorld();
});

Hooks.on("preCreateActor", (createData) => {
    mergeObject(createData, {
        "token.bar1" :{ "attribute" : "wounds" },
        "token.bar2" :{ "attribute" : "fatigue" },
        "token.displayName" : CONST.TOKEN_DISPLAY_MODES.HOVER,
        "token.displayBars" : CONST.TOKEN_DISPLAY_MODES.ALWAYS,
        "token.disposition" : CONST.TOKEN_DISPOSITIONS.NEUTRAL,
        "token.name" : createData.name
    });
    if (createData.type === "acolyte") {
        createData.token.vision = true;
        createData.token.actorLink = true;
    }
});