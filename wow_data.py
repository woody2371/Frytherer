# https://us.api.battle.net/wow/data/character/races?locale=en_US&apikey=
wow_races = {
    "races": [{
        "id": 1,
        "mask": 1,
        "side": "alliance",
        "name": "Human"
    }, {
        "id": 2,
        "mask": 2,
        "side": "horde",
        "name": "Orc"
    }, {
        "id": 3,
        "mask": 4,
        "side": "alliance",
        "name": "Dwarf"
    }, {
        "id": 4,
        "mask": 8,
        "side": "alliance",
        "name": "Night Elf"
    }, {
        "id": 5,
        "mask": 16,
        "side": "horde",
        "name": "Undead"
    }, {
        "id": 6,
        "mask": 32,
        "side": "horde",
        "name": "Tauren"
    }, {
        "id": 7,
        "mask": 64,
        "side": "alliance",
        "name": "Gnome"
    }, {
        "id": 8,
        "mask": 128,
        "side": "horde",
        "name": "Troll"
    }, {
        "id": 9,
        "mask": 256,
        "side": "horde",
        "name": "Goblin"
    }, {
        "id": 10,
        "mask": 512,
        "side": "horde",
        "name": "Blood Elf"
    }, {
        "id": 11,
        "mask": 1024,
        "side": "alliance",
        "name": "Draenei"
    }, {
        "id": 22,
        "mask": 2097152,
        "side": "alliance",
        "name": "Worgen"
    }, {
        "id": 24,
        "mask": 8388608,
        "side": "neutral",
        "name": "Pandaren"
    }, {
        "id": 25,
        "mask": 16777216,
        "side": "alliance",
        "name": "Pandaren"
    }, {
        "id": 26,
        "mask": 33554432,
        "side": "horde",
        "name": "Pandaren"
    }]
}

# https://us.api.battle.net/wow/data/character/classes?locale=en_US&apikey=
wow_classes = {
    "classes": [{
        "id": 3,
        "mask": 4,
        "powerType": "focus",
        "name": "Hunter"
    }, {
        "id": 4,
        "mask": 8,
        "powerType": "energy",
        "name": "Rogue"
    }, {
        "id": 1,
        "mask": 1,
        "powerType": "rage",
        "name": "Warrior"
    }, {
        "id": 2,
        "mask": 2,
        "powerType": "mana",
        "name": "Paladin"
    }, {
        "id": 7,
        "mask": 64,
        "powerType": "mana",
        "name": "Shaman"
    }, {
        "id": 8,
        "mask": 128,
        "powerType": "mana",
        "name": "Mage"
    }, {
        "id": 5,
        "mask": 16,
        "powerType": "mana",
        "name": "Priest"
    }, {
        "id": 6,
        "mask": 32,
        "powerType": "runic-power",
        "name": "Death Knight"
    }, {
        "id": 11,
        "mask": 1024,
        "powerType": "mana",
        "name": "Druid"
    }, {
        "id": 12,
        "mask": 2048,
        "powerType": "fury",
        "name": "Demon Hunter"
    }, {
        "id": 9,
        "mask": 256,
        "powerType": "mana",
        "name": "Warlock"
    }, {
        "id": 10,
        "mask": 512,
        "powerType": "energy",
        "name": "Monk"
    }]
}

# https://us.api.battle.net/wow/data/talents?locale=en_US&apikey=
wow_talents = {
    "1": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 202297,
                        "name": "Dauntless",
                        "icon": "ability_warrior_unrelentingassault",
                        "description": "Your abilities cost 20% less Rage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 46968,
                        "name": "Shockwave",
                        "icon": "ability_warrior_shockwave",
                        "description": "Sends a wave of force in a frontal cone, causing 10,374 damage and stunning all enemies within 10 yards for 4 sec.  Cooldown reduced by 20 sec if it strikes at least 3 targets.",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 215556,
                        "name": "War Machine",
                        "icon": "ability_hunter_rapidkilling",
                        "description": "Killing a target grants you 30% Haste and 30% movement speed for 10 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 202296,
                        "name": "Endless Rage",
                        "icon": "ability_warrior_endlessrage",
                        "description": "Your auto attack generates 30% additional Rage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 107570,
                        "name": "Storm Bolt",
                        "icon": "warrior_talent_icon_stormbolt",
                        "description": "Hurls your weapon at an enemy, causing 21,841 Physical damage and stunning for 4 sec.",
                        "range": "20 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 7384,
                        "name": "Overpower",
                        "icon": "ability_meleedamage",
                        "description": "Overpowers the enemy, causing 96,413 Physical damage. Cannot be blocked, dodged or parried, and has a 60% increased chance to critically strike.\n\n\n\nAll your melee attacks have a chance to activate Overpower.",
                        "range": "Melee Range",
                        "powerCost": "10 Rage",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 103828,
                        "name": "Warbringer",
                        "icon": "ability_warrior_warbringer",
                        "description": "Charge now deals 23,588 damage to all enemies within 5 yds of the target, and stuns them for 1.5 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 202161,
                        "name": "Sweeping Strikes",
                        "icon": "ability_rogue_slicedice",
                        "description": "Mortal Strike and Execute hit a second nearby target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 215568,
                        "name": "Fresh Meat",
                        "icon": "ability_deathwing_bloodcorruption_death",
                        "description": "Bloodthirst has a 40% increased critical strike chance against targets above 80% health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 46968,
                        "name": "Shockwave",
                        "icon": "ability_warrior_shockwave",
                        "description": "Sends a wave of force in a frontal cone, causing 10,374 damage and stunning all enemies within 10 yards for 4 sec.  Cooldown reduced by 20 sec if it strikes at least 3 targets.",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 46968,
                        "name": "Shockwave",
                        "icon": "ability_warrior_shockwave",
                        "description": "Sends a wave of force in a frontal cone, causing 10,374 damage and stunning all enemies within 10 yards for 4 sec.  Cooldown reduced by 20 sec if it strikes at least 3 targets.",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 202168,
                        "name": "Impending Victory",
                        "icon": "spell_impending_victory",
                        "description": "Instantly attack the target, causing 52,419 damage and healing you for 15% of your maximum health.\n\n\n\nKilling an enemy that yields experience or honor resets the cooldown of Impending Victory.",
                        "range": "Melee Range",
                        "powerCost": "10 Rage",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 107570,
                        "name": "Storm Bolt",
                        "icon": "warrior_talent_icon_stormbolt",
                        "description": "Hurls your weapon at an enemy, causing 21,841 Physical damage and stunning for 4 sec.",
                        "range": "20 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 107570,
                        "name": "Storm Bolt",
                        "icon": "warrior_talent_icon_stormbolt",
                        "description": "Hurls your weapon at an enemy, causing 21,841 Physical damage and stunning for 4 sec.",
                        "range": "20 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 205484,
                        "name": "Inspiring Presence",
                        "icon": "ability_toughness",
                        "description": "You inspire your party or raid members within 60 yards, causing them to be healed for 3% of all damage they deal.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 223657,
                        "name": "Safeguard",
                        "icon": "ability_warrior_safeguard",
                        "description": "Intercepting a friendly target now also causes 20% of their damage taken to transfer to you for 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 103827,
                        "name": "Double Time",
                        "icon": "inv_misc_horn_04",
                        "description": "Increases the maximum number of charges on Charge by 1, and reduces its cooldown by 3 sec.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 202316,
                        "name": "Fervor of Battle",
                        "icon": "ability_rogue_waylay",
                        "description": "Whirlwind deals 30% increased damage to your primary target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 202288,
                        "name": "Renewed Fury",
                        "icon": "ability_warrior_intensifyrage",
                        "description": "Ignore Pain also enrages you, increasing all damage you deal by 10% for 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 215569,
                        "name": "Wrecking Ball",
                        "icon": "ability_butcher_whirl",
                        "description": "Your attacks have a chance to make your next Whirlwind deal 200% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 206320,
                        "name": "Outburst",
                        "icon": "spell_nature_ancestralguardian",
                        "description": "Berserker Rage now causes Enrage.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 772,
                        "name": "Rend",
                        "icon": "ability_gouge",
                        "description": "Wounds the target, causing 117,945 Bleed damage over 15 sec.",
                        "range": "Melee Range",
                        "powerCost": "15 Rage",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 122509,
                        "name": "Ultimatum",
                        "icon": "ability_warrior_stalwartprotector",
                        "description": "Your Shield Slam critical strikes cause your next Focused Rage to cost no Rage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 107574,
                        "name": "Avatar",
                        "icon": "warrior_talent_icon_avatar",
                        "description": "Transform into a colossus for 20 sec, causing you to deal 20% increased damage and removing all roots and snares.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 202224,
                        "name": "Furious Charge",
                        "icon": "spell_warrior_barbarian",
                        "description": "Charge also increases the healing from your next Bloodthirst by 300%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 29838,
                        "name": "Second Wind",
                        "icon": "ability_hunter_harass",
                        "description": "Restores 6% health every 1 sec when you have not taken damage for 5 sec.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 223662,
                        "name": "Warlord's Challenge",
                        "icon": "ability_racial_bloodrage",
                        "description": "While Berserker Rage is active, you may use Taunt with no cooldown and Taunted enemies move 50% faster towards you.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 202163,
                        "name": "Bounding Stride",
                        "icon": "ability_heroicleap",
                        "description": "Reduces the cooldown on Heroic Leap by 15 sec, and Heroic Leap now also increases your run speed by 70% for 3 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 197690,
                        "name": "Defensive Stance",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A defensive combat state that reduces all damage you take by 20%, and all damage you deal by 10%. Lasts until cancelled.",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 208154,
                        "name": "Warpaint",
                        "icon": "ability_rogue_preparation",
                        "description": "You now take only 15% increased damage from Enrage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 203201,
                        "name": "Crackling Thunder",
                        "icon": "ability_thunderking_overcharge",
                        "description": "Increases the radius of Thunder Clap by 100%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 202560,
                        "name": "Best Served Cold",
                        "icon": "ability_warrior_revenge",
                        "description": "Revenge generates 2 additional Rage for each target that it hits.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 206315,
                        "name": "Massacre",
                        "icon": "inv_sword_48",
                        "description": "Execute critical strikes reduce the Rage cost of your next Rampage by 100%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 215550,
                        "name": "In For The Kill",
                        "icon": "ability_blackhand_marked4death",
                        "description": "Mortal Strike refunds 20 Rage when used against targets that are below 20% health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 202593,
                        "name": "Mortal Combo",
                        "icon": "ability_warrior_savageblow",
                        "description": "Mortal Strike now has a maximum of 2 charges.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 215571,
                        "name": "Frothing Berserker",
                        "icon": "warrior_talent_icon_furyintheblood",
                        "description": "When you reach 100 Rage, your damage is increased by 10% and your movement speed by 30% for 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 202561,
                        "name": "Never Surrender",
                        "icon": "ability_butcher_gushingwounds",
                        "description": "Ignore Pain will ignore up to 75% more damage, based on your missing health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 202095,
                        "name": "Indomitable",
                        "icon": "ability_warrior_intensifyrage",
                        "description": "Increases your maximum health by 25%, and the maximum effect of Ignore Pain by 25%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 202922,
                        "name": "Carnage",
                        "icon": "ability_warrior_rampage",
                        "description": "Reduces the cost of Rampage by 15 Rage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 207982,
                        "name": "Focused Rage",
                        "icon": "ability_warrior_focusedrage",
                        "description": "Focus your rage on your next Mortal Strike, increasing its damage by 30%, stacking up to 3 times. Unaffected by the global cooldown",
                        "range": "Melee Range",
                        "powerCost": "15 Rage",
                        "castTime": "Instant",
                        "cooldown": "1.5 sec cooldown"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 227266,
                        "name": "Deadly Calm",
                        "icon": "achievement_boss_kingymiron",
                        "description": "Battle Cry also reduces the Rage cost of your abilities by 100% for the duration.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 202572,
                        "name": "Vengeance",
                        "icon": "ability_warrior_unrelentingassault",
                        "description": "Ignore Pain reduces the Rage cost of your next Focused Rage by 35%, and Focused Rage reduces the Rage cost of your next Ignore Pain by 35%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 12292,
                        "name": "Bloodbath",
                        "icon": "ability_warrior_bloodbath",
                        "description": "For 10 sec, your melee attacks and abilities cause the target to bleed for 40% additional damage over 6 sec.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 202603,
                        "name": "Into the Fray",
                        "icon": "ability_warrior_bloodfrenzy",
                        "description": "You gain 3% Haste for each enemy within 10 yards, up to 5 enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 215538,
                        "name": "Trauma",
                        "icon": "ability_warrior_trauma",
                        "description": "Slam and Whirlwind now cause the target to bleed for 20% additional damage over 6 sec. Multiple uses accumulate increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 206313,
                        "name": "Frenzy",
                        "icon": "inv_axe_2h_orcwarrior_c_01",
                        "description": "Furious Slash increases your Haste by 5% for 10 sec, stacking up to 3 times.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 202612,
                        "name": "Titanic Might",
                        "icon": "ability_warrior_colossussmash",
                        "description": "Increases the duration of Colossus Smash by 16 sec, but reduces its effectiveness by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 202743,
                        "name": "Booming Voice",
                        "icon": "ability_warrior_battleshout",
                        "description": "Demoralizing Shout also generates 50 Rage, and increases damage you deal to affected targets by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 215573,
                        "name": "Inner Rage",
                        "icon": "ability_warrior_innerrage",
                        "description": "Raging Blow no longer requires Enrage and deals 150% increased damage, but has a 4.5 sec cooldown.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 152278,
                        "name": "Anger Management",
                        "icon": "warrior_talent_icon_angermanagement",
                        "description": "Every 10 Rage you spend reduces the remaining cooldown on Battle Cry, Last Stand, and Shield Wall by 1 sec.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 46924,
                        "name": "Bladestorm",
                        "icon": "ability_warrior_bladestorm",
                        "description": "Become an unstoppable storm of destructive force, striking all targets within 8 yards for 282,556 Physical damage over 5.5 sec.\n\n\n\nYou are immune to movement impairing and loss of control effects, but can use defensive abilities and can avoid attacks.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 202751,
                        "name": "Reckless Abandon",
                        "icon": "ability_warrior_battleshout",
                        "description": "Battle Cry generates 100 Rage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 203179,
                        "name": "Opportunity Strikes",
                        "icon": "ability_backstab",
                        "description": "Your melee abilities have up to a 60% chance, based on the target's missing health, to trigger an extra attack that deals 41,136 Physical damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 203177,
                        "name": "Heavy Repercussions",
                        "icon": "inv_shield_32",
                        "description": "Shield Slam extends the duration of Shield Block by 1.5 sec, and Shield Block increases the damage of Shield Slam by an additional 30%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 118000,
                        "name": "Dragon Roar",
                        "icon": "ability_warrior_dragonroar",
                        "description": "Roar explosively, dealing 35,382 damage to all enemies within 8 yards and increasing all damage you deal by 20% for 6 sec. Dragon Roar ignores all armor and always critically strikes.",
                        "castTime": "Instant",
                        "cooldown": "25 sec cooldown"
                    },
                    "spec": {
                        "name": "Fury",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-fury",
                        "icon": "ability_warrior_innerrage",
                        "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 228920,
                        "name": "Ravager",
                        "icon": "warrior_talent_icon_ravager",
                        "description": "Throws a whirling weapon at the target location that inflicts 412,804 damage to all enemies within 8 yards over 6.4 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-warrior-protection",
                        "icon": "ability_warrior_defensivestance",
                        "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 152277,
                        "name": "Ravager",
                        "icon": "warrior_talent_icon_ravager",
                        "description": "Throws a whirling weapon at the target location that inflicts 412,804 damage to all enemies within 8 yards over 6.4 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Arms",
                        "role": "DPS",
                        "backgroundImage": "bg-warrior-arms",
                        "icon": "ability_warrior_savageblow",
                        "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
                        "order": 0
                    }
                }]
            ]
        ],
        "class": "warrior",
        "specs": [{
            "name": "Arms",
            "role": "DPS",
            "backgroundImage": "bg-warrior-arms",
            "icon": "ability_warrior_savageblow",
            "description": "A battle-hardened master of two-handed weapons, using mobility and overpowering attacks to strike his opponents down.",
            "order": 0
        }, {
            "name": "Fury",
            "role": "DPS",
            "backgroundImage": "bg-warrior-fury",
            "icon": "ability_warrior_innerrage",
            "description": "A furious berserker wielding a weapon in each hand, unleashing a flurry of attacks to carve her opponents to pieces.",
            "order": 1
        }, {
            "name": "Protection",
            "role": "TANK",
            "backgroundImage": "bg-warrior-protection",
            "icon": "ability_warrior_defensivestance",
            "description": "A stalwart protector who uses a shield to safeguard herself and her allies.",
            "order": 2
        }]
    },
    "2": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 152261,
                        "name": "Holy Shield",
                        "icon": "spell_holy_blessingofprotection",
                        "description": "Increases your block chance by 10%, allows you to block spells, and your successful blocks deal 16,382 Holy damage to your attacker.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 223306,
                        "name": "Bestow Faith",
                        "icon": "ability_paladin_blessedmending",
                        "description": "Infuse a friendly target with faith for 5 sec, healing them for 36,036 at the end.",
                        "range": "40 yd range",
                        "powerCost": "6% of base mana",
                        "castTime": "Instant",
                        "cooldown": "12 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 198038,
                        "name": "Final Verdict",
                        "icon": "spell_paladin_templarsverdict",
                        "description": "Increases the damage done by Templar's Verdict by 20%, and the damage done by Divine Storm by 10%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 114158,
                        "name": "Light's Hammer",
                        "icon": "spell_paladin_lightshammer",
                        "description": "Hurls a Light-infused hammer into the ground, where it blasts a 10 yard radius every 2 sec for 14 sec. Each blast deals 6,200 Holy damage to enemies and heals up to 6 allies for 3,003.",
                        "range": "40 yd range",
                        "powerCost": "35% of base mana",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 213757,
                        "name": "Execution Sentence",
                        "icon": "spell_paladin_executionsentence",
                        "description": "A hammer slowly falls from the sky, dealing 240,251 Holy damage after 6.4 sec.",
                        "range": "20 yd range",
                        "powerCost": "3 Holy Power",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 204019,
                        "name": "Blessed Hammer",
                        "icon": "paladin_retribution",
                        "description": "Throws a Blessed Hammer that spirals outward, dealing 12,537 Holy damage to enemies that it hits, and causing them to deal 15% less damage to you on their next auto attack.",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 196926,
                        "name": "Crusader's Might",
                        "icon": "ability_paladin_swiftretribution",
                        "description": "Crusader Strike reduces the cooldown of Holy Shock and Light of Dawn by 1.5 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 205228,
                        "name": "Consecration",
                        "icon": "spell_holy_innerfire",
                        "description": "Consecrates the land beneath you, causing 71,729 Holy damage over 10.9 sec to enemies who enter the area.",
                        "castTime": "Instant",
                        "cooldown": "12 sec cooldown"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 203785,
                        "name": "Consecrated Hammer",
                        "icon": "inv_hammer_01",
                        "description": "Hammer of the Righteous has no cooldown.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 203776,
                        "name": "First Avenger",
                        "icon": "ability_skyreach_shielded",
                        "description": "Avenger's Shield now deals 50% increased damage to the first target hit. Grand Crusader now has an additional 10% chance to occur.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 203316,
                        "name": "The Fires of Justice",
                        "icon": "spell_holy_crusaderstrike",
                        "description": "Reduces the cooldown of Crusader Strike by 1.0 sec and gives it a 15% chance to reduce the cost of your next damaging or healing Holy Power ability by 1.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 230332,
                        "name": "Cavalier",
                        "icon": "ability_paladin_divinesteed",
                        "description": "Divine Steed now has 2 charges.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 114154,
                        "name": "Unbreakable Spirit",
                        "icon": "spell_holy_unyieldingfaith",
                        "description": "Reduces the cooldown of your Divine Shield, Divine Protection, and Lay on Hands by 30%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 217020,
                        "name": "Zeal",
                        "icon": "spell_holy_sealofblood",
                        "description": "Strike the target for 82,273 Physical damage. Maximum 2 charges.\n\n\n\nGrants Zeal, causing Zeal attacks to chain to an additional nearby target per stack. Maximum 3 stacks. Each jump deals 40% less damage.\n\n\n\nGenerates 1 Holy Power.",
                        "range": "Melee Range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 204035,
                        "name": "Bastion of Light",
                        "icon": "paladin_protection",
                        "description": "Immediately grants 3 charges of Shield of the Righteous.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 218178,
                        "name": "Greater Judgment",
                        "icon": "spell_holy_righteousfury",
                        "description": "Your Judgment ability hits 2 additional nearby enemies, and always deals a critical strike against targets above 50% health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 204023,
                        "name": "Crusader's Judgment",
                        "icon": "ability_paladin_enlightenedjudgements",
                        "description": "Judgment now has 2 charges, and Grand Crusader now also grants a charge of Judgment.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 214202,
                        "name": "Rule of Law",
                        "icon": "ability_paladin_longarmofthelaw",
                        "description": "Increase the range of your heals by 50% for 10 sec.",
                        "castTime": "Instant",
                        "cooldown": "1.5 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 198054,
                        "name": "Fist of Justice",
                        "icon": "spell_holy_fistofjustice",
                        "description": "Judgment reduces the remaining cooldown on Hammer of Justice by 10 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 20066,
                        "name": "Repentance",
                        "icon": "spell_holy_prayerofhealing",
                        "description": "Forces an enemy target to meditate, incapacitating the target and dealing up to a maximum of 25% of the target's health in damage over 1 min. Usable against Demons, Dragonkin, Giants, Humanoids, and Undead.",
                        "range": "30 yd range",
                        "powerCost": "10% of base mana",
                        "castTime": "1.7 sec cast",
                        "cooldown": "15 sec cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 115750,
                        "name": "Blinding Light",
                        "icon": "ability_paladin_blindinglight",
                        "description": "Emits dazzling light in all directions, blinding enemies within 10 yards, dealing 16,217 Holy damage and causing them to wander disoriented for 6 sec. Non-Holy damage will break the disorient effect.",
                        "powerCost": "8% of base mana",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 204018,
                        "name": "Blessing of Spellwarding",
                        "icon": "spell_holy_blessingofprotection",
                        "description": "Places a blessing on a party or raid member, protecting them from all magical attacks for 10 sec. Cannot be used on a target with Forbearance.  Causes Forbearance for 30 sec.",
                        "range": "40 yd range",
                        "powerCost": "15% of base mana",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 183425,
                        "name": "Devotion Aura",
                        "icon": "spell_holy_devotionaura",
                        "description": "Allies within 10 yards take 20% reduced damage, split over the number of allies in the aura.\n\n\n\nWhile Aura Mastery is active, all affected allies gain the full damage reduction.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 202271,
                        "name": "Virtue's Blade",
                        "icon": "ability_paladin_bladeofjustice",
                        "description": "Blade of Justice critical strikes now deal 3 times normal damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 231832,
                        "name": "Blade of Wrath",
                        "icon": "ability_paladin_bladeofjusticeblue",
                        "description": "Your auto attacks have a chance to reset the cooldown of Blade of Justice.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 183416,
                        "name": "Aura of Sacrifice",
                        "icon": "ability_deathwing_bloodcorruption_earth",
                        "description": "While you are above 75% health, 10% of all damage taken by allies within 10 yds is redirected to you. \n\n\n\nWhile Aura Mastery is active, 15% of all effective healing you deal is replicated to all allies in the aura.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 230332,
                        "name": "Cavalier",
                        "icon": "ability_paladin_divinesteed",
                        "description": "Divine Steed now has 2 charges.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 198034,
                        "name": "Divine Hammer",
                        "icon": "classicon_paladin",
                        "description": "Divine Hammers spin around you, damaging enemies within 8 yds for 11,569 Holy damage instantly and every 2 sec for 10.9 sec.\n\n\n\nGenerates 2 Holy Power.",
                        "castTime": "Instant",
                        "cooldown": "12 sec cooldown"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 203797,
                        "name": "Retribution Aura",
                        "icon": "spell_holy_auraoflight",
                        "description": "Protects yourself and all party or raid members within 60 yards with an aura that deals 983 Holy damage when melee attacked.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 183415,
                        "name": "Aura of Mercy",
                        "icon": "spell_holy_blessedlife",
                        "description": "Restores 901 health to 3 injured allies within 10 yds every 1 sec.\n\n\n\nWhile Aura Mastery is active, heals all allies in the aura instead of 3 and healing is increased by 100%.",
                        "castTime": "Passive",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 215661,
                        "name": "Justicar's Vengeance",
                        "icon": "spell_holy_retributionaura",
                        "description": "A weapon strike that deals 174,728 Holy damage and restores health equal to the damage done.\n\n\n\nDeals 100% additional damage and healing when used against a stunned target.",
                        "range": "Melee Range",
                        "powerCost": "5 Holy Power",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 213652,
                        "name": "Hand of the Protector",
                        "icon": "ability_paladin_blessedhands",
                        "description": "Calls down the Light to heal a friendly target for 30% of the target's missing health.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 197646,
                        "name": "Divine Purpose",
                        "icon": "spell_holy_divinepurpose",
                        "description": "Light of Dawn and Holy Shock have a 15% chance to not start their cooldown, and make their next cast free.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 105809,
                        "name": "Holy Avenger",
                        "icon": "ability_paladin_holyavenger",
                        "description": "Increases your haste by 30% and your Holy Shock healing by 30% for 20 sec.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 204139,
                        "name": "Knight Templar",
                        "icon": "ability_mount_charger",
                        "description": "Reduces the cooldown of Divine Steed by 50% and reduces all damage taken while mounted on your Divine Steed by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 205191,
                        "name": "Eye for an Eye",
                        "icon": "spell_paladin_inquisition",
                        "description": "Reduces Physical damage you take by 35%, and instantly counterattacks any enemy that strikes you in melee combat for 43,707 Physical damage.  Lasts 10 sec.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 210191,
                        "name": "Word of Glory",
                        "icon": "inv_helmet_96",
                        "description": "Heal yourself and up to 5 friendly targets within 15 yards for 54,055. Maximum 2 charges.",
                        "powerCost": "3 Holy Power",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 204077,
                        "name": "Final Stand",
                        "icon": "spell_holy_crusade",
                        "description": "When you use Divine Shield, you also taunt all targets within 15 yards for 8 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 114165,
                        "name": "Holy Prism",
                        "icon": "spell_paladin_holyprism",
                        "description": "A beam of light turns the target into a Holy Prism.\n\n\n\nAn enemy target takes 18,020 Holy damage and radiates 12,012 healing to 5 nearby allies within 15 yards.\n\n\n\nA friendly target is healed for 24,024 and radiates 13,513 Holy damage to 5 nearby enemies within 15 yards.",
                        "range": "40 yd range",
                        "powerCost": "17% of base mana",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 204150,
                        "name": "Aegis of Light",
                        "icon": "spell_holy_greaterblessingoflight",
                        "description": "Channels an Aegis of Light that protects you and all allies standing within 10 yards behind you for 6 sec, reducing all damage taken by 20%.",
                        "castTime": "Channeled",
                        "cooldown": "5 min cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 213313,
                        "name": "Divine Intervention",
                        "icon": "spell_nature_timestop",
                        "description": "Reduces your Divine Shield cooldown by 50%.  In addition, any attack which would kill you instead reduces you to 20% of your maximum health and triggers Divine Shield.\n\n\n\nCannot occur while Divine Shield is on cooldown or Forbearance is active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 196923,
                        "name": "Fervent Martyr",
                        "icon": "ability_paladin_selflesshealer",
                        "description": "Casting Holy Light or Flash of Light on your Beacon of Light reduces the cost of your next Light of the Martyr by 50%, stacking.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 230332,
                        "name": "Cavalier",
                        "icon": "ability_paladin_divinesteed",
                        "description": "Divine Steed now has 2 charges.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 183778,
                        "name": "Judgment of Light",
                        "icon": "spell_holy_divineprovidence",
                        "description": "Judgment now applies Judgment of Light to the target, causing the next 40 successful attacks against the target to heal the attacker for 1,201. This effect can only occur once per 1 sec on each target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 53376,
                        "name": "Sanctified Wrath",
                        "icon": "ability_paladin_sanctifiedwrath",
                        "description": "Avenging Wrath lasts 25% longer and also reduces Holy Shock's cooldown by 50% for its duration.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 202273,
                        "name": "Seal of Light",
                        "icon": "spell_holy_sealofvengeance",
                        "description": "Infuse yourself with holy energy, increasing your movement speed by 20%.\n\n\n\nLasts 20 sec per Holy Power spent.",
                        "powerCost": "1 Holy Power",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 183778,
                        "name": "Judgment of Light",
                        "icon": "spell_holy_divineprovidence",
                        "description": "Judgment now applies Judgment of Light to the target, causing the next 40 successful attacks against the target to heal the attacker for 1,201. This effect can only occur once per 1 sec on each target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 204054,
                        "name": "Consecrated Ground",
                        "icon": "ability_paladin_enlightenedjudgements",
                        "description": "Up to 6 allies standing within your Consecration receive 499 healing every 1 sec, and enemies within your Consecration have 50% reduced movement speed.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 204074,
                        "name": "Righteous Protector",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Shield of the Righteous reduces the remaining cooldown on Light of the Protector and Avenging Wrath by 3 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 223817,
                        "name": "Divine Purpose",
                        "icon": "spell_holy_divinepurpose",
                        "description": "Your Holy Power spending abilities have a 20% chance to make your next Holy Power spending ability free.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 156910,
                        "name": "Beacon of Faith",
                        "icon": "ability_paladin_beaconsoflight",
                        "description": "Mark a second target as a Beacon, mimicking the effects of Beacon of Light. Your heals will now heal both of your Beacons, but at 20% reduced effectiveness.",
                        "range": "60 yd range",
                        "powerCost": "3.12% of base mana",
                        "castTime": "Instant",
                        "cooldown": "3 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 231895,
                        "name": "Crusade",
                        "icon": "ability_paladin_sanctifiedwrath",
                        "description": "Increases your damage and haste by 3.5% for 20 sec.\n\n\n\nEach Holy Power spent during Crusade increases damage and haste by an additional 3.5%.\n\n\n\nMaximum 15 stacks.",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 197446,
                        "name": "Beacon of the Lightbringer",
                        "icon": "spell_paladin_clarityofpurpose",
                        "description": "Mastery: Lightbringer now increases your healing based on the target's proximity to either you or your Beacon of Light, whichever is closer.\n\n\n\nThe healing and range of Light of Dawn are increased by 30%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 152262,
                        "name": "Seraphim",
                        "icon": "ability_paladin_seraphim",
                        "description": "The Light temporarily magnifies your power, increasing your Haste, Critical Strike, Mastery, and Versatility by 4,881.\n\n\n\nConsumes up to 2 charges of Shield of the Righteous, and lasts 8 sec per charge.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 200025,
                        "name": "Beacon of Virtue",
                        "icon": "ability_paladin_beaconofinsight",
                        "description": "Apply a Beacon of Light to your target and 3 injured allies within 30 yards for 8 sec. Your heals will heal all of them for 40% of the amount healed.",
                        "range": "40 yd range",
                        "powerCost": "15% of base mana",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-paladin-holy",
                        "icon": "spell_holy_holybolt",
                        "description": "Invokes the power of the Light to protect and to heal.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 203791,
                        "name": "Last Defender",
                        "icon": "spell_holy_divinepurpose",
                        "description": "Each enemy within 8 yards reduces the damage that you take and increases the damage that you deal by 3%. This effect has diminishing returns.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Protection",
                        "role": "TANK",
                        "backgroundImage": "bg-paladin-protection",
                        "icon": "ability_paladin_shieldofthetemplar",
                        "description": "Uses Holy magic to shield himself and defend allies from attackers.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 210220,
                        "name": "Holy Wrath",
                        "icon": "spell_holy_vindication",
                        "description": "Deals 200% of your missing health in Holy damage to 4 nearby enemies, up to 120% of your maximum health.\n\n\n\nDeals 50% of missing health against enemy players.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Retribution",
                        "role": "DPS",
                        "backgroundImage": "bg-paladin-retribution",
                        "icon": "spell_holy_auraoflight",
                        "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
                        "order": 2
                    }
                }]
            ]
        ],
        "class": "paladin",
        "specs": [{
            "name": "Holy",
            "role": "HEALING",
            "backgroundImage": "bg-paladin-holy",
            "icon": "spell_holy_holybolt",
            "description": "Invokes the power of the Light to protect and to heal.",
            "order": 0
        }, {
            "name": "Protection",
            "role": "TANK",
            "backgroundImage": "bg-paladin-protection",
            "icon": "ability_paladin_shieldofthetemplar",
            "description": "Uses Holy magic to shield himself and defend allies from attackers.",
            "order": 1
        }, {
            "name": "Retribution",
            "role": "DPS",
            "backgroundImage": "bg-paladin-retribution",
            "icon": "spell_holy_auraoflight",
            "description": "A righteous crusader who judges and punishes opponents with weapons and Holy magic.",
            "order": 2
        }]
    },
    "3": {
        "petSpecs": [{
            "name": "Ferocity",
            "role": "DPS",
            "backgroundImage": "bg-deathknight-blood",
            "icon": "ability_druid_kingofthejungle",
            "description": "Driven by a frenzied persistence to pursue prey, these beasts stop at nothing to achieve victory; even death is temporary for these predators.",
            "order": 0
        }, {
            "name": "Ferocity",
            "role": "DPS",
            "backgroundImage": "bg-rogue-assassination",
            "icon": "ability_druid_kingofthejungle",
            "description": "Driven by a rabid persistence to pursue prey, these carnivorous beasts stop at nothing to achieve victory; even death is temporary for these predators.",
            "order": 0
        }, {
            "name": "Tenacity",
            "role": "TANK",
            "backgroundImage": "bg-deathknight-blood",
            "icon": "ability_druid_demoralizingroar",
            "description": "Stalwart and veteran defenders who unquestionably place their thick hides and protective exteriors in harm's way for their allies.",
            "order": 1
        }, {
            "name": "Tenacity",
            "role": "TANK",
            "backgroundImage": "bg-rogue-assassination",
            "icon": "ability_druid_demoralizingroar",
            "description": "Stalwart and veteran defenders who unquestionably place their thick hides and protective exteriors in harm's way for their allies.",
            "order": 1
        }, {
            "name": "Cunning",
            "role": "DPS",
            "backgroundImage": "bg-rogue-assassination",
            "icon": "ability_eyeoftheowl",
            "description": "Guileful creatures capable of skillfully mitigating lethal blows dealt to themselves and their allies.",
            "order": 2
        }, {
            "name": "Cunning",
            "role": "DPS",
            "backgroundImage": "bg-deathknight-blood",
            "icon": "ability_eyeoftheowl",
            "description": "Guileful creatures capable of skillfully mitigating lethal blows dealt to themselves and their allies.",
            "order": 2
        }],
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 204308,
                        "name": "Big Game Hunter",
                        "icon": "ability_hunter_efficiency",
                        "description": "Increases the critical strike chance of your auto shot and Cobra Shot by 50% on targets who are above 80% health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 204315,
                        "name": "Animal Instincts",
                        "icon": "ability_druid_predatoryinstincts",
                        "description": "Flanking Strike also reduces the remaining cooldown by 2.7 sec of a random one of the following abilities:\n\n\n\n Flanking Strike\n\n Mongoose Bite\n\n Aspect of the Eagle\n\n Harpoon",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 155228,
                        "name": "Lone Wolf",
                        "icon": "spell_hunter_lonewolf",
                        "description": "Increases your damage by 18%, but you can no longer use Call Pet.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 193533,
                        "name": "Steady Focus",
                        "icon": "ability_hunter_improvedsteadyshot",
                        "description": "Using Arcane Shot or Multi-Shot three times in a row increases your Focus Regeneration by 25% for 12 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 200163,
                        "name": "Throwing Axes",
                        "icon": "inv_throwingaxepvp320_07",
                        "description": "Tosses 3 axes at an enemy, each dealing 68,253 Physical damage.",
                        "range": "30 yd range",
                        "powerCost": "15 Focus",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 194397,
                        "name": "Way of the Cobra",
                        "icon": "ability_hunter_cobrastrikes",
                        "description": "Cobra Shot deals 8% increased damage for every pet or guardian you have active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 193532,
                        "name": "Dire Stable",
                        "icon": "ability_hunter_sickem",
                        "description": "Dire Beast generates 12 additional Focus over its duration.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 201082,
                        "name": "Way of the Mok'Nathal",
                        "icon": "achievement_character_orc_male_brn",
                        "description": "Raptor Strike also grants you Mok'Nathal Tactics, increasing your attack power by 3% for 8 sec, stacking up to 4 times.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 53238,
                        "name": "Careful Aim",
                        "icon": "ability_hunter_zenarchery",
                        "description": "Aimed Shot, Arcane Shot, Marked Shot, and Multi-Shot have 20% increased critical strike chance against targets above 80% Health, and those critical strikes deal an additional 30% damage over 8 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 206505,
                        "name": "A Murder of Crows",
                        "icon": "ability_hunter_murderofcrows",
                        "description": "Summons a flock of crows to attack your target over the next 15 sec. If the target dies while under attack, A Murder of Crows' cooldown is reset.",
                        "range": "40 yd range",
                        "powerCost": "30 Focus",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 194595,
                        "name": "Lock and Load",
                        "icon": "ability_hunter_lockandload",
                        "description": "Your ranged auto attacks have a 8% chance to trigger Lock and Load, causing your next two Aimed Shots to cost no Focus and be instant.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 199530,
                        "name": "Stomp",
                        "icon": "warrior_talent_icon_thunderstruck",
                        "description": "When your Dire Beasts charge in, they will stomp the ground, dealing 176,997 Physical damage to all nearby enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 201075,
                        "name": "Mortal Wounds",
                        "icon": "ability_warrior_bloodbath",
                        "description": "Each time Lacerate deals damage, you have a 2% chance to gain a charge of Mongoose Bite.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 217200,
                        "name": "Dire Frenzy",
                        "icon": "ability_druid_mangle",
                        "description": "Causes your pet to enter a frenzy, performing a flurry of 5 attacks on the target, and gaining 30% increased attack speed for 8 sec, stacking up to 3 times.\n\n\n\nGenerates 25 Focus.",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 194599,
                        "name": "Black Arrow",
                        "icon": "spell_shadow_painspike",
                        "description": "Fires a Black Arrow at the target, dealing 239,888 Shadow damage over 8 sec and summoning a Dark Minion to taunt it for the duration.\n\n\n\nWhen you kill an enemy, the remaining cooldown on Black Arrow will reset.",
                        "range": "40 yd range",
                        "powerCost": "40 Focus",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 53209,
                        "name": "Chimaera Shot",
                        "icon": "ability_hunter_chimerashot2",
                        "description": "A two-headed shot that hits your primary target and another nearby target, dealing 44,032 Nature damage to one and 44,032 Frost damage to the other. Generates 10 Focus for every target hit.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "9 sec cooldown"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 201078,
                        "name": "Snake Hunter",
                        "icon": "achievement_boss_epochhunter",
                        "description": "Instantly grants you 3 charges of Mongoose Bite.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 199527,
                        "name": "True Aim",
                        "icon": "spell_hunter_focusingshot",
                        "description": "Each successive Arcane Shot or Aimed Shot fired at the same target increases the damage those Shots deal to the target by 2%, stacking up to 8 times. Limit 1 target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 109215,
                        "name": "Posthaste",
                        "icon": "ability_hunter_posthaste",
                        "description": "Disengage also frees you from all movement impairing effects and increases your movement speed by 60% for 5 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 199523,
                        "name": "Farstrider",
                        "icon": "ability_hunter_pet_chimera",
                        "description": "Your ability critical strikes have a 10% chance to reset the remaining cooldown on Disengage.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 199921,
                        "name": "Trailblazer",
                        "icon": "ability_hunter_aspectmastery",
                        "description": "Your movement speed is increased by 30% anytime you have not attacked for 3 seconds.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 199528,
                        "name": "One with the Pack",
                        "icon": "icon_upgradestone_beast_uncommon",
                        "description": "Grants Wild Call 15% increased chance to reset the cooldown on Dire Beast.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 212431,
                        "name": "Explosive Shot",
                        "icon": "ability_hunter_explosiveshot",
                        "description": "Fires a slow-moving munition directly forward. Activating this ability a second time detonates the Shot, dealing up to 218,410 Fire damage to all enemies within 8 yds, damage based on proximity.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 194277,
                        "name": "Caltrops",
                        "icon": "ability_ironmaidens_incindiarydevice",
                        "description": "Scatters Caltrops in an area for 15 sec. Enemies who step on Caltrops will take 5,460 Bleed damage every 1 sec, and have 70% reduced movement speed for 6 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 199518,
                        "name": "Improved Traps",
                        "icon": "inv_pet_pettrap",
                        "description": "Reduces the cooldown of Freezing Trap by 15% and the cooldown of Explosive Trap and Tar Trap by 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 194306,
                        "name": "Bestial Fury",
                        "icon": "ability_hunter_fervor",
                        "description": "Increase the damage bonus of Bestial Wrath by 15%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 206817,
                        "name": "Sentinel",
                        "icon": "spell_nature_sentinal",
                        "description": "Applies Hunter's Mark to all enemies near the target.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1.5 sec cooldown"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 130392,
                        "name": "Blink Strikes",
                        "icon": "spell_arcane_arcane04",
                        "description": "Your pet's Basic Attack deals 50% increased damage, can now be used from 30 yards away, and will instantly teleport your pet behind its target. Your pet can teleport only once per 20 sec.",
                        "range": "100 yd range",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 213423,
                        "name": "Patient Sniper",
                        "icon": "ability_hunter_snipertraining",
                        "description": "Gain the patience of a veteran sniper, increasing your maximum focus by 30 and causing Vulnerable to increase your Marked Shot and Aimed Shot damage by 150%, but only last 6 sec and no longer stack.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 162488,
                        "name": "Steel Trap",
                        "icon": "inv_pet_pettrap02",
                        "description": "Hurls a Steel Trap to the target location that immobilizes the first enemy that approaches for 30 sec and deals 327,615 bleed damage over 30 sec. Other damage may break the immobilization effect. Limit 1. Trap will exist for 1 min.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 191241,
                        "name": "Sticky Bomb",
                        "icon": "inv_misc_bomb_08",
                        "description": "Hurls a concussive grenade at your target which sticks to them and explodes after 3 sec, knocking back all nearby enemies.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 109248,
                        "name": "Binding Shot",
                        "icon": "spell_shaman_bindelemental",
                        "description": "Fires a magical projectile, tethering the enemy and any other enemies within 5 yards for 10 sec, stunning them for 5 sec if they move more than 5 yards from the arrow.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 200108,
                        "name": "Ranger's Net",
                        "icon": "inv_misc_net_01",
                        "description": "Hurls a net at the enemy, rooting the target for 3 sec and reducing movement speed by 50% for 15 sec. Damage may break the effect.",
                        "range": "40 yd range",
                        "powerCost": "30 Focus",
                        "castTime": "Instant",
                        "cooldown": "1 sec cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 19386,
                        "name": "Wyvern Sting",
                        "icon": "inv_spear_02",
                        "description": "A stinging shot that puts the target to sleep, incapacitating them for 30 sec. Damage will cancel the effect. Usable while moving.",
                        "range": "40 yd range",
                        "castTime": "1.5 sec cast",
                        "cooldown": "45 sec cooldown"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 199483,
                        "name": "Camouflage",
                        "icon": "ability_hunter_camouflage",
                        "description": "You and your pet blend into the surroundings and gain stealth for 1 min. While camouflaged, you will heal for 2% every 1 secs.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 199483,
                        "name": "Camouflage",
                        "icon": "ability_hunter_camouflage",
                        "description": "You and your pet blend into the surroundings and gain stealth for 1 min. While camouflaged, you will heal for 2% every 1 secs.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 19577,
                        "name": "Intimidation",
                        "icon": "ability_devour",
                        "description": "Commands your pet to intimidate the target, stunning it for 5 sec.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 131894,
                        "name": "A Murder of Crows",
                        "icon": "ability_hunter_murderofcrows",
                        "description": "Summons a flock of crows to attack your target, dealing 1,195,744 Physical damage over 15 sec. When a target dies while affected by this ability, its cooldown will reset.",
                        "range": "40 yd range",
                        "powerCost": "30 Focus",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 212436,
                        "name": "Butchery",
                        "icon": "ability_butcher_cleave",
                        "description": "Strike all nearby enemies in a flurry of strikes, inflicting 133,205 Physical damage to each.",
                        "range": "8 yd range",
                        "powerCost": "40 Focus",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 194855,
                        "name": "Dragonsfire Grenade",
                        "icon": "spell_fire_incinerate",
                        "description": "Hurls a dragonsfire grenade at the target that explodes into flames, inflicting 279,563 Fire damage over 8 sec and reducing movement speed by 20%. The volatile flames on the target also scorch nearby enemies.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 120360,
                        "name": "Barrage",
                        "icon": "ability_hunter_rapidregeneration",
                        "description": "Rapidly fires a spray of shots for 2.7 sec, dealing 570,174 Physical damage to the target and an average of 285,087 Physical damage to each other enemy in front of you. Usable while moving.",
                        "range": "40 yd range",
                        "powerCost": "60 Focus",
                        "castTime": "Channeled",
                        "cooldown": "20 sec cooldown"
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 87935,
                        "name": "Serpent Sting",
                        "icon": "ability_hunter_serpentswiftness",
                        "description": "Targets hit by your Raptor Strike and Carve are also affected by Serpent Sting, dealing 95,010 Nature damage over 15 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 194386,
                        "name": "Volley",
                        "icon": "ability_marksmanship",
                        "description": "While active, your auto attacks spend 3 Focus to also launch a volley of shots that hit the target and all other nearby enemies, dealing 46,131 additional Physical damage.",
                        "castTime": "Instant",
                        "cooldown": "1.5 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 214579,
                        "name": "Sidewinders",
                        "icon": "ability_hunter_serpentswiftness",
                        "description": "Launches Sidewinders that travel toward the target, weaving back and forth and dealing 65,523 Nature damage to each target they hit. Cannot hit the same target twice. Applies Vulnerable to all targets hit.\n\n\n\nGenerates 50 Focus.\n\n\n\nAlso replaces Multi-Shot.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 194407,
                        "name": "Spitting Cobra",
                        "icon": "ability_hunter_cobrastrikes",
                        "description": "Summons a Spitting Cobra for 30 sec that attacks your target for 4,369 Nature damage every 2 sec. While the Cobra is active you gain an extra 3 Focus every 1 sec.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 201430,
                        "name": "Stampede",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "Summon a herd of stampeding animals from the wilds around you that deal damage to your enemies for 12 sec.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 198670,
                        "name": "Piercing Shot",
                        "icon": "ability_cheapshot",
                        "description": "A powerful shot which deals up to 697,505 Physical damage to the target and up to 348,752 Physical damage to all enemies between you and the target.",
                        "range": "40 yd range",
                        "powerCost": "20 Focus",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 199543,
                        "name": "Expert Trapper",
                        "icon": "inv_pet_pettrap02",
                        "description": "All of your traps are improved in the following ways:\n\n\n\nFreezing Trap\n\nWhen Freezing Trap's incapacitate effect ends, the victim and all neaby enemies' movement speed is reduced by 50% for 4 sec.\n\n\n\nExplosive Trap\n\nIncreases Explosive Trap's damage to the triggering enemy by 75%.\n\n\n\nTar Trap\n\nEnemies moving through the tar have a chance to be rooted in place for 4 sec.\n\n\n\nSteel Trap\n\nYour Steel Trap also deals an immediate 109,205 Bleed damage when triggered.\n\n\n\nCaltrops\n\nIncreases Caltrops damage by 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Survival",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-survival",
                        "icon": "ability_hunter_camouflage",
                        "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 199532,
                        "name": "Killer Cobra",
                        "icon": "ability_hunter_snaketrap",
                        "description": "While Bestial Wrath is active, Cobra Shot resets the cooldown on Kill Command.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Beast Mastery",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-beastmaster",
                        "icon": "ability_hunter_bestialdiscipline",
                        "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 199522,
                        "name": "Trick Shot",
                        "icon": "ability_hunter_runningshot",
                        "description": "Aimed Shot will now also ricochet and hit all Vulnerable targets for 30% of normal damage.\n\n\n\nIf there are no other Vulnerable targets, the damage of your next Aimed Shot is increased by 15%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Marksmanship",
                        "role": "DPS",
                        "backgroundImage": "bg-hunter-marksman",
                        "icon": "ability_hunter_focusedaim",
                        "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 191384,
                        "name": "Aspect of the Beast",
                        "icon": "ability_deathwing_assualtaspects",
                        "description": "Kill Command and Flanking Strike cause an additional effect, based on your pet's Specialization.\n\n\n\nFerocity\n\nThe target also bleeds for 29,487 Physical damage over 6 sec.\n\n\n\nTenacity\n\nYour pet also takes 15% reduced damage for 6 sec.\n\n\n\nCunning\n\nThe target's movement speed is also reduced by 50% for 4 sec.",
                        "castTime": "Passive"
                    }
                }]
            ]
        ],
        "class": "hunter",
        "specs": [{
            "name": "Beast Mastery",
            "role": "DPS",
            "backgroundImage": "bg-hunter-beastmaster",
            "icon": "ability_hunter_bestialdiscipline",
            "description": "A master of the wild who can tame a wide variety of beasts to assist her in combat.",
            "order": 0
        }, {
            "name": "Marksmanship",
            "role": "DPS",
            "backgroundImage": "bg-hunter-marksman",
            "icon": "ability_hunter_focusedaim",
            "description": "A master archer or sharpshooter who excels in bringing down enemies from afar.",
            "order": 1
        }, {
            "name": "Survival",
            "role": "DPS",
            "backgroundImage": "bg-hunter-survival",
            "icon": "ability_hunter_camouflage",
            "description": "A rugged tracker who favors using animal venom, explosives and traps as deadly weapons.",
            "order": 2
        }]
    },
    "4": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 196864,
                        "name": "Master Poisoner",
                        "icon": "ability_creature_poison_06",
                        "description": "Increases the damage done by your poisons by 30% and their non-damaging effects by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 31223,
                        "name": "Master of Subtlety",
                        "icon": "ability_rogue_masterofsubtlety",
                        "description": "Attacks made while stealthed and for 6 seconds after breaking stealth cause an additional 10% damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 196937,
                        "name": "Ghostly Strike",
                        "icon": "ability_creature_cursed_02",
                        "description": "Strikes an enemy with your cursed weapon, dealing 49,880 Physical damage and causing the target to take 10% increased damage from your abilities for 15 sec.\n\n\n\nAwards 1 combo point.",
                        "range": "Melee Range",
                        "powerCost": "30 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 200733,
                        "name": "Swordmaster",
                        "subtext": "Passive Talent",
                        "icon": "inv_sword_97",
                        "description": "Saber Slash has a 10% increased chance to strike an additional time.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 193537,
                        "name": "Weaponmaster",
                        "icon": "ability_ironmaidens_bladerush",
                        "description": "Your abilities have a 6% chance to hit the target twice each time they deal damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 193640,
                        "name": "Elaborate Planning",
                        "icon": "inv_misc_map08",
                        "description": "Your finishing moves grant 15% increased damage done for 5 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 196938,
                        "name": "Quick Draw",
                        "subtext": "Passive Talent",
                        "icon": "inv_weapon_rifle_40",
                        "description": "Free uses of Pistol Shot granted by Sabre Slash now generate 1 additional combo point, and deal 50% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 16511,
                        "name": "Hemorrhage",
                        "icon": "spell_shadow_lifedrain",
                        "description": "Rips a gushing wound in the target, dealing 25,710 Physical damage and increasing Bleed damage from your abilities on the target by 25% for 20 sec.\n\n\n\nAwards 1 combo point.",
                        "range": "Melee Range",
                        "powerCost": "30 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 200758,
                        "name": "Gloomblade",
                        "icon": "ability_ironmaidens_convulsiveshadows",
                        "description": "Punctures your target with your shadow-infused blade for 109,286 Shadow damage.\n\n\n\nAwards 1 combo point.",
                        "range": "Melee Range",
                        "powerCost": "35 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 14062,
                        "name": "Nightstalker",
                        "subtext": "Passive Talent",
                        "icon": "ability_stealth",
                        "description": "While Stealth is active, you move 20% faster and your abilities deal 50% more damage.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 195457,
                        "name": "Grappling Hook",
                        "icon": "ability_rogue_grapplinghook",
                        "description": "Launch a grappling hook and pull yourself to the target location.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 196924,
                        "name": "Acrobatic Strikes",
                        "subtext": "Passive Talent",
                        "icon": "spell_warrior_wildstrike",
                        "description": "Increases the range on all your melee attacks by 3 yards.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 108208,
                        "name": "Subterfuge",
                        "icon": "rogue_subterfuge",
                        "description": "Your abilities requiring Stealth can still be used for 3 sec after Stealth breaks.\n\n\n\nAlso causes Garrote to deal 100% increased damage and have no cooldown when used from Stealth or 3 sec after Stealth breaks.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 196922,
                        "name": "Hit and Run",
                        "subtext": "Passive Talent",
                        "icon": "ability_rogue_fleetfooted",
                        "description": "Increases your movement speed at all times by 15%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 108209,
                        "name": "Shadow Focus",
                        "icon": "rogue_shadowfocus",
                        "description": "Abilities cost 50% less Energy while Stealth is active.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 193531,
                        "name": "Deeper Stratagem",
                        "icon": "archaeology_5_0_changkiboard",
                        "description": "You may have a maximum of 6 combo points, your finishing moves consume up to 6 combo points, and your finishing moves deal 10% increased damage.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 114015,
                        "name": "Anticipation",
                        "icon": "ability_rogue_slaughterfromtheshadows",
                        "description": "You may have a maximum of 8 combo points. Finishers still consume a maximum of 5 combo points.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 14983,
                        "name": "Vigor",
                        "icon": "ability_rogue_vigor",
                        "description": "Increases your maximum Energy by 50 and your Energy regeneration by 10%.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 108211,
                        "name": "Leeching Poison",
                        "icon": "rogue_leeching_poison",
                        "description": "Coats your weapons with a Non-Lethal Poison that lasts for 1 hour, granting you 10% Leech.",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 200759,
                        "name": "Soothing Darkness",
                        "icon": "spell_shadow_twilight",
                        "description": "You heal 3% of your maximum life every 1 sec while Stealth is active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 193546,
                        "name": "Iron Stomach",
                        "icon": "inv_misc_organ_11",
                        "description": "Increases the healing you receive from Crimson Vial, healing potions, and healthstones by 30%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 79008,
                        "name": "Elusiveness",
                        "subtext": "Passive Talent",
                        "icon": "ability_rogue_turnthetables",
                        "description": "Feint also reduces all damage you take from non-area-of-effect attacks by 30% for 5 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 31230,
                        "name": "Cheat Death",
                        "subtext": "Passive Talent",
                        "icon": "ability_rogue_cheatdeath",
                        "description": "Fatal attacks instead reduce you to 7% of your maximum health. For 3 sec afterward, you take 85% reduced damage. Cannot trigger more often than once per 2 min.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 196951,
                        "name": "Strike from the Shadows",
                        "subtext": "Passive Talent",
                        "icon": "ability_rogue_unfairadvantage",
                        "description": "Shadowstrike also stuns your target for 2 sec. Players are Dazed for 5 sec instead.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 199743,
                        "name": "Parley",
                        "icon": "achievement_character_human_male",
                        "description": "Pacifies a target not in combat, who is forced to negotiate instead of fighting for 5 min. Only works on Humanoids, Demons, and Dragonkin. Damage caused will break the peace. Limit 1.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 196861,
                        "name": "Thuggee",
                        "icon": "inv_misc_bandana_03",
                        "description": "Resets the remaining cooldown on Garrote when a target dies with your Garrote active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 131511,
                        "name": "Prey on the Weak",
                        "icon": "ability_rogue_preyontheweak",
                        "description": "Enemies disabled with your Kidney Shot, Cheap Shot, or Sap take 10% increased damage from all sources.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 154904,
                        "name": "Internal Bleeding",
                        "icon": "ability_rogue_bloodsplatter",
                        "description": "Kidney Shot also deals 27,126 Bleed damage per combo point over 12 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 200778,
                        "name": "Tangled Shadow",
                        "subtext": "Passive Talent",
                        "icon": "inv_misc_volatileshadow",
                        "description": "Nightblade now decreases the target's movement speed by an additional 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 108216,
                        "name": "Dirty Tricks",
                        "subtext": "Passive Talent",
                        "icon": "ability_rogue_dirtydeeds",
                        "description": "Gouge, Blind, Cheap Shot, and Sap no longer cost Energy.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 196979,
                        "name": "Premeditation",
                        "subtext": "Passive",
                        "icon": "spell_shadow_possession",
                        "description": "Cheap Shot and Shadowstrike generate 1 additional combo point.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 185767,
                        "name": "Cannonball Barrage",
                        "icon": "ability_rogue_cannonballbarrage",
                        "description": "Command a ghost ship crew to barrage the target area with cannonballs doing 157,260 Physical damage over 1.8 sec and slowing enemies by 50% for 1.5 sec.",
                        "range": "35 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 200802,
                        "name": "Agonizing Poison",
                        "icon": "inv_poison_mindnumbing",
                        "description": "Coats your weapons with a Lethal Poison that lasts for 1 hour. Each strike has a 20% chance to poison the enemy for 12 sec, increasing all damage taken from your abilities by 4.0%, stacking up to 5 times.\n\n\n\nDamage bonus increased by Mastery: Potent Poisons.",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 193539,
                        "name": "Alacrity",
                        "icon": "ability_paladin_speedoflight",
                        "description": "Your finishing moves have a 20% chance per combo point to grant 1% Haste for 20 sec, stacking up to 20 times.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 51690,
                        "name": "Killing Spree",
                        "icon": "ability_rogue_murderspree",
                        "description": "Teleport to an enemy within 10 yards, attacking 7 times over 3 sec for 53,991 Physical damage with your main-hand and 13,105 Physical damage with your off-hand.\n\n\n\nWhile Blade Flurry is active, each Killing Spree attack will teleport to and damage a different nearby enemy target.",
                        "range": "10 yd range",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 206237,
                        "name": "Enveloping Shadows",
                        "icon": "ability_rogue_envelopingshadows",
                        "description": "Finishing move that generates 1 combo point every 3 sec. Lasts longer per combo point spent.\n\n   1 point  : 6 seconds\n\n   2 points: 12 seconds\n\n   3 points: 18 seconds\n\n   4 points: 24 seconds\n\n   5 points: 30 seconds",
                        "powerCost": "30 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 200806,
                        "name": "Exsanguinate",
                        "icon": "ability_deathwing_bloodcorruption_earth",
                        "description": "Twist your blades into the target's wounds, causing your Bleed effects on them to bleed out 100% faster.",
                        "range": "Melee Range",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 152152,
                        "name": "Venom Rush",
                        "icon": "rogue_venomzest",
                        "description": "Venomous Wounds grants 3 additional Energy each time it grants Energy.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Assassination",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-assassination",
                        "icon": "ability_rogue_deadlybrew",
                        "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 5171,
                        "name": "Slice and Dice",
                        "icon": "ability_rogue_slicedice",
                        "description": "Finishing move that consumes combo points to increase attack speed by 100%. Lasts longer per combo point.\n\n   1 point  : 12 seconds\n\n   2 points: 18 seconds\n\n   3 points: 24 seconds\n\n   4 points: 30 seconds\n\n   5 points: 36 seconds",
                        "powerCost": "25 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Outlaw",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-combat",
                        "icon": "inv_sword_30",
                        "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 196976,
                        "name": "Master of Shadows",
                        "subtext": "Passive",
                        "icon": "spell_shadow_charm",
                        "description": "You immediately gain 30 Energy when you enter Stealth or activate Shadow Dance.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Subtlety",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_stealth",
                        "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 137619,
                        "name": "Marked for Death",
                        "icon": "achievement_bg_killingblow_berserker",
                        "description": "Marks the target, instantly generating 5 combo points. Cooldown reset if the target dies within 1 min.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 152150,
                        "name": "Death from Above",
                        "icon": "spell_rogue_deathfromabove",
                        "description": "Finishing move that empowers your weapons with shadow energy and performs a devastating two-part attack. \n\n\n\nYou whirl around, dealing up to 79,939 damage to all enemies within 8 yds, then leap into the air and Eviscerate your target on the way back down, with such force that it has a 50% stronger effect.",
                        "range": "15 yd range",
                        "powerCost": "25 Energy",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    }
                }]
            ]
        ],
        "class": "rogue",
        "specs": [{
            "name": "Assassination",
            "role": "DPS",
            "backgroundImage": "bg-rogue-assassination",
            "icon": "ability_rogue_deadlybrew",
            "description": "A deadly master of poisons who dispatches victims with vicious dagger strikes.",
            "order": 0
        }, {
            "name": "Outlaw",
            "role": "DPS",
            "backgroundImage": "bg-rogue-combat",
            "icon": "inv_sword_30",
            "description": "A ruthless fugitive who uses agility and guile to stand toe-to-toe with enemies.",
            "order": 1
        }, {
            "name": "Subtlety",
            "role": "DPS",
            "backgroundImage": "bg-rogue-subtlety",
            "icon": "ability_stealth",
            "description": "A dark stalker who leaps from the shadows to ambush his unsuspecting prey.",
            "order": 2
        }]
    },
    "5": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 200347,
                        "name": "The Penitent",
                        "icon": "spell_priest_finalprayer",
                        "description": "Penance may be cast on a friendly target, healing them for 54,054 over 1.8 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Discipline",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-discipline",
                        "icon": "spell_holy_powerwordshield",
                        "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 109142,
                        "name": "Twist of Fate",
                        "icon": "spell_shadow_mindtwisting",
                        "description": "After healing a target below 35% health, you deal 20% increased damage and 20% increased healing for 10 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 200128,
                        "name": "Trail of Light",
                        "icon": "ability_priest_wordsofmeaning",
                        "description": "When you cast Flash Heal, 40% of the healing is replicated to the previous target you healed with Flash Heal.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 193134,
                        "name": "Castigation",
                        "icon": "spell_holy_searinglightpriest",
                        "description": "Penance fires one additional bolt of holy light over its duration.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 200153,
                        "name": "Enduring Renewal",
                        "icon": "priest_icon_chakra",
                        "description": "Your single-target healing spells refresh the duration of your Renew on the target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 193195,
                        "name": "Fortress of the Mind",
                        "icon": "ability_mage_studentofthemind",
                        "description": "Mind Flay and Mind Blast deal 10% more damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 193155,
                        "name": "Enlightenment",
                        "icon": "spell_arcane_mindmastery",
                        "description": "You regenerate mana 10% faster.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 205351,
                        "name": "Shadow Word: Void",
                        "icon": "spell_mage_presenceofmind",
                        "description": "Blasts the target's mind for 13,214 Shadow damage.",
                        "range": "40 yd range",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 214621,
                        "name": "Schism",
                        "icon": "spell_warlock_focusshadow",
                        "description": "Attack the enemy's soul with a surge of Shadow energy, dealing 25,526 Shadow damage and increasing damage that you deal to the target by 30% for 6 sec.",
                        "range": "40 yd range",
                        "powerCost": "2.5% of base mana",
                        "castTime": "1.5 sec cast",
                        "cooldown": "6 sec cooldown"
                    },
                    "spec": {
                        "name": "Discipline",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-discipline",
                        "icon": "spell_holy_powerwordshield",
                        "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 193173,
                        "name": "Mania",
                        "icon": "spell_shadow_skull",
                        "description": "You move 1% faster for every 5 Insanity you have.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 121536,
                        "name": "Angelic Feather",
                        "icon": "ability_priest_angelicfeather",
                        "description": "Places a feather at the target location, granting the first ally to walk through it 40% increased movement speed for 5 sec. Only 3 feathers can be placed at one time.  Maximum 3 charges.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 214121,
                        "name": "Body and Mind",
                        "icon": "spell_holy_persecution",
                        "description": "Heals the target for 3,604 every 1 sec and increases their movement speed by 40% for 4 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 64129,
                        "name": "Body and Soul",
                        "icon": "spell_holy_symbolofhope",
                        "description": "Power Word: Shield and Leap of Faith increase your target's movement speed by 40% for 3 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 193063,
                        "name": "Masochism",
                        "icon": "spell_shadow_misery",
                        "description": "When you cast Shadow Mend on yourself, its damage over time effect heals you instead.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 19236,
                        "name": "Desperate Prayer",
                        "icon": "spell_holy_testoffaith",
                        "description": "Heals you for 30% of your maximum health, and increases your maximum health by 30%, decreasing by 2% every second.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 204263,
                        "name": "Shining Force",
                        "icon": "ability_paladin_blindinglight2",
                        "description": "Creates a burst of light around a friendly target, knocking away nearby enemies and slowing their movement speed by 70% for 3 sec.",
                        "range": "40 yd range",
                        "powerCost": "2.5% of base mana",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 205369,
                        "name": "Mind Bomb",
                        "icon": "spell_shadow_mindbomb",
                        "description": "Inflicts the target with a Mind Bomb.\n\n\n\nAfter 2 sec, or if the target dies, it unleashes a psychic explosion, stunning all enemies within 8 yds of the target for 2 sec.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 196704,
                        "name": "Psychic Voice",
                        "icon": "spell_shadow_psychichorrors",
                        "description": "Reduces the cooldown of Psychic Scream by 30 sec.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 200199,
                        "name": "Censure",
                        "icon": "spell_holy_eyeforaneye",
                        "description": "Holy Word: Chastise stuns the target for 5 sec and is not broken by damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 205367,
                        "name": "Dominant Mind",
                        "icon": "spell_priest_voidflay",
                        "description": "You may also control your own character while Mind Control is active, but Mind Control has a 2 min cooldown, and it may not be used against players.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 196707,
                        "name": "Afterlife",
                        "icon": "inv_enchant_essencemagiclarge",
                        "description": "Increases the duration of Spirit of Redemption by 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 196985,
                        "name": "Light of the Naaru",
                        "icon": "inv_pet_naaru",
                        "description": "Serendipity reduces the remaining cooldown on the appropriate Holy Word by an additional 2 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 129250,
                        "name": "Power Word: Solace",
                        "subtext": "Talent",
                        "icon": "ability_priest_flashoflight",
                        "description": "Strikes an enemy with heavenly power, dealing 18,018 Holy damage and restoring 1.00% of your maximum mana.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "12 sec cooldown"
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 199849,
                        "name": "Void Lord",
                        "icon": "warlock_summon_voidlord",
                        "description": "Lingering Insanity persists for 8 seconds after you next enter Void Form.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 200209,
                        "name": "Guardian Angel",
                        "icon": "ability_priest_pathofthedevout",
                        "description": "When Guardian Spirit expires without saving the target from death, reduce its remaining cooldown to 90 seconds.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 199853,
                        "name": "Reaper of Souls",
                        "icon": "ability_warlock_soulswap",
                        "description": "Shadow Word: Death is now castable on targets below 35% health, and always generates Insanity as though it killed the target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 197045,
                        "name": "Shield Discipline",
                        "icon": "spell_holy_divineprotection",
                        "description": "When your Power Word: Shield is completely absorbed you instantly regenerate 1% of your maximum mana.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 123040,
                        "name": "Mindbender",
                        "icon": "spell_shadow_soulleech_3",
                        "description": "Summons a Mindbender to attack the target for 12 sec. You regenerate 0.50% of maximum mana each time the Mindbender attacks.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 64901,
                        "name": "Symbol of Hope",
                        "icon": "spell_holy_symbolofhope",
                        "description": "Bolster the morale of all healers in your party or raid within 40 yards, allowing them to cast spells for no mana for 10 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "6 min cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 205371,
                        "name": "Void Ray",
                        "icon": "spell_priest_voidsear",
                        "description": "Each time your Mind Flay or Mind Sear deals damage, you gain 10% increased Mind Flay and Mind Sear damage for 6 sec, stacking up to 4 times.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 199855,
                        "name": "San'layn",
                        "icon": "achievement_boss_lanathel",
                        "description": "Increases the damage of your Vampiric Touch by 20%, and the healing of your Vampiric Embrace by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 109186,
                        "name": "Surge of Light",
                        "icon": "spell_holy_surgeoflight",
                        "description": "Your healing spells and Smite have a 8% chance to make your next Flash Heal instant and cost no mana. Maximum 2 charges.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 197419,
                        "name": "Contrition",
                        "icon": "ability_priest_savinggrace",
                        "description": "Increases Atonement duration by 3 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Discipline",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-discipline",
                        "icon": "spell_holy_powerwordshield",
                        "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 155271,
                        "name": "Auspicious Spirits",
                        "icon": "ability_priest_auspiciousspirits",
                        "description": "Your Shadowy Apparitions now deal 100% increased damage and generate 4 Insanity.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 10060,
                        "name": "Power Infusion",
                        "icon": "spell_holy_powerinfusion",
                        "description": "Infuses you with power for 20 sec, increasing haste by 25% and reducing the mana cost of all spells by 20%.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 32546,
                        "name": "Binding Heal",
                        "icon": "spell_holy_blindingheal",
                        "description": "Heals you, another friendly target, and a third friendly target within 20 yards for 18,018.\n\n\n\nTriggers Serendipity, reducing the remaining cooldown on both Holy Word: Serenity and Holy Word: Sanctify by 3 sec.",
                        "range": "40 yd range",
                        "powerCost": "2.5% of base mana",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 162452,
                        "name": "Shadowy Insight",
                        "icon": "spell_shadow_possession",
                        "description": "Shadow Word: Pain periodic damage has a 10% chance to reset the remaining cooldown on Mind Blast and cause your next Mind Blast to be instant.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 109142,
                        "name": "Twist of Fate",
                        "icon": "spell_shadow_mindtwisting",
                        "description": "After healing a target below 35% health, you deal 20% increased damage and 20% increased healing for 10 sec.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 197034,
                        "name": "Piety",
                        "icon": "ability_priest_bindingprayers",
                        "description": "Prayer of Mending now triggers Serendipity, reducing the remaining cooldown on Holy Word: Sanctify.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 152118,
                        "name": "Clarity of Will",
                        "icon": "ability_priest_clarityofwill",
                        "description": "Shields the target with a protective ward for 20 sec, absorbing 54,054 damage.",
                        "range": "40 yd range",
                        "powerCost": "2.79% of base mana",
                        "castTime": "2 sec cast"
                    },
                    "spec": {
                        "name": "Discipline",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-discipline",
                        "icon": "spell_holy_powerwordshield",
                        "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 197031,
                        "name": "Divinity",
                        "icon": "ability_priest_ascendance",
                        "description": "When you heal with a Holy Word spell, your healing is increased by 15% for 6 sec.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 10060,
                        "name": "Power Infusion",
                        "icon": "spell_holy_powerinfusion",
                        "description": "Infuses you with power for 20 sec, increasing haste by 25% and reducing the mana cost of all spells by 20%.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 205385,
                        "name": "Shadow Crash",
                        "icon": "spell_shadow_shadowfury",
                        "description": "Hurl a bolt of slow-moving Shadow energy at the destination, dealing 38,438 Shadow damage to all targets within 8 yards.\n\n\n\nGenerates 15 Insanity.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 110744,
                        "name": "Divine Star",
                        "icon": "spell_priest_divinestar",
                        "description": "Throw a Divine Star forward 24 yds, healing allies in its path for 5,406 and dealing 8,710 Holy damage to enemies. After reaching its destination, the Divine Star returns to you, healing allies and damaging enemies in its path again.",
                        "range": "30 yd range",
                        "powerCost": "2.5% of base mana",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 120517,
                        "name": "Halo",
                        "icon": "ability_priest_halo",
                        "description": "Creates a ring of Holy energy around you that quickly expands to a 30 yd radius, healing allies for 17,261 and dealing 25,892 Holy damage to enemies.",
                        "range": "30 yd range",
                        "powerCost": "3.59% of base mana",
                        "castTime": "1.5 sec cast",
                        "cooldown": "40 sec cooldown"
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 200174,
                        "name": "Mindbender",
                        "icon": "spell_shadow_soulleech_3",
                        "description": "Summons a Mindbender to attack the target for 15 sec.\n\n\n\nGenerates 4 Insanity each time the Mindbender attacks.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 193225,
                        "name": "Legacy of the Void",
                        "icon": "inv_enchant_voidcrystal",
                        "description": "Voidform may be activated anytime your Insanity level is 70 or higher.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 200183,
                        "name": "Apotheosis",
                        "icon": "ability_priest_ascension",
                        "description": "Enter a pure Holy form for 30 sec, increasing the effects of Serendipity by 200% and reducing the cost of your Holy Words by 100%.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 204197,
                        "name": "Purge the Wicked",
                        "icon": "ability_mage_firestarter",
                        "description": "Cleanses the target with fire, causing 6,006 Fire damage and an additional 28,830 Fire damage over 20 sec. Spreads to an additional nearby enemy when you cast Penance on the target.",
                        "range": "40 yd range",
                        "powerCost": "2% of base mana",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Discipline",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-discipline",
                        "icon": "spell_holy_powerwordshield",
                        "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 193157,
                        "name": "Benediction",
                        "icon": "spell_monk_diffusemagic",
                        "description": "Your Prayer of Mending has a 50% chance to leave a Renew on each target it heals.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 200309,
                        "name": "Grace",
                        "subtext": "Passive",
                        "icon": "spell_holy_hopeandgrace",
                        "description": "Increases your non-Atonement healing and absorption by 30% on targets with Atonement.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 73510,
                        "name": "Mind Spike",
                        "icon": "spell_priest_mindspike",
                        "description": "Assail the target with shadowy spikes, dealing 2,703 Shadowfrost damage and leaving a spike embedded in their mind.\n\n\n\nMind Blast will detonate these spikes, each dealing 200% of their original damage to the main target, and 100% to all nearby targets.\n\n\n\nGenerates 4 Insanity.",
                        "range": "40 yd range",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 204883,
                        "name": "Circle of Healing",
                        "icon": "spell_holy_circleofrenewal",
                        "description": "Heals up to 5 injured allies within 30 yards of the target for 15,616.",
                        "range": "40 yd range",
                        "powerCost": "5% of base mana",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Holy",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-holy",
                        "icon": "spell_holy_guardianspirit",
                        "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 193223,
                        "name": "Surrender to Madness",
                        "icon": "achievement_boss_generalvezax_01",
                        "description": "All your Insanity-generating abilities generate 150% more Insanity, and you can cast while moving, until you exit Voidform.\n\n\n\nThen you die. Horribly.",
                        "castTime": "Instant",
                        "cooldown": "10 min cooldown"
                    },
                    "spec": {
                        "name": "Shadow",
                        "role": "DPS",
                        "backgroundImage": "bg-priest-shadow",
                        "icon": "spell_shadow_shadowwordpain",
                        "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 204065,
                        "name": "Shadow Covenant",
                        "icon": "spell_shadow_summonvoidwalker",
                        "description": "Draws on the power of shadow to heal up to 5 injured allies within 30 yds of the target for 33,033, but leaves a shell on them that absorbs the next 16,516 healing they receive within 6 sec.",
                        "range": "40 yd range",
                        "powerCost": "5% of base mana",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Discipline",
                        "role": "HEALING",
                        "backgroundImage": "bg-priest-discipline",
                        "icon": "spell_holy_powerwordshield",
                        "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
                        "order": 0
                    }
                }]
            ]
        ],
        "class": "priest",
        "specs": [{
            "name": "Discipline",
            "role": "HEALING",
            "backgroundImage": "bg-priest-discipline",
            "icon": "spell_holy_powerwordshield",
            "description": "Uses magic to shield allies from taking damage as well as heal their wounds.",
            "order": 0
        }, {
            "name": "Holy",
            "role": "HEALING",
            "backgroundImage": "bg-priest-holy",
            "icon": "spell_holy_guardianspirit",
            "description": "A versatile healer who can reverse damage on individuals or groups and even heal from beyond the grave.",
            "order": 1
        }, {
            "name": "Shadow",
            "role": "DPS",
            "backgroundImage": "bg-priest-shadow",
            "icon": "spell_shadow_shadowwordpain",
            "description": "Uses sinister Shadow magic, especially damage-over-time spells, to eradicate enemies.",
            "order": 2
        }]
    },
    "6": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 207057,
                        "name": "Shattering Strikes",
                        "icon": "ability_warrior_shatteringthrow",
                        "description": "If there are 5 stacks of Razorice on the target, Frost Strike will consume them and deal 40% additional damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 194916,
                        "name": "All Will Serve",
                        "icon": "ability_fiegndead",
                        "description": "Your Raise Dead spell summons an additional skeletal minion, and its cooldown is removed.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 195679,
                        "name": "Bloodworms",
                        "icon": "spell_shadow_soulleech",
                        "description": "Your auto attack critical strikes have a chance to summon a Bloodworm.\n\n\n\nBloodworms deal minor damage to your target for 15 sec and then burst, healing you for 5% of your missing health.\n\n\n\nIf you drop below 50% health, your Bloodworms will immediately burst and heal you.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 194878,
                        "name": "Icy Talons",
                        "icon": "spell_deathknight_icytalons",
                        "description": "Frost Strike also increases your melee attack speed by 10% for 6 sec, stacking up to 3 times.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 207264,
                        "name": "Bursting Sores",
                        "icon": "ability_druid_infectedwound",
                        "description": "Festering Wounds deal 50% more damage when burst, and all enemies within 8 yds of a burst Festering Wound suffer 19,657 Shadow damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 221536,
                        "name": "Heartbreaker",
                        "icon": "spell_deathknight_deathstrike",
                        "description": "Heart Strike generates 3 additional Runic Power per target hit.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 207269,
                        "name": "Ebon Fever",
                        "icon": "spell_shadow_creepingplague",
                        "description": "Virulent Plague deals the same damage in half the time.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 206931,
                        "name": "Blooddrinker",
                        "icon": "ability_animusdraw",
                        "description": "Drains 282,405 health from the target over 3 sec.\n\n\n\nYou can move, parry, dodge, and use defensive abilities while channeling this ability.",
                        "range": "30 yd range",
                        "castTime": "Channeled",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 207061,
                        "name": "Murderous Efficiency",
                        "icon": "spell_frost_frostarmor",
                        "description": "Consuming the Killing Machine effect has a 50% chance to cause you to gain 1 Rune.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 207317,
                        "name": "Epidemic",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "Causes each of your Virulent Plagues within 100 yds to flare up, dealing 32,762 Shadow damage to the infected enemy, and an additional 6,006 Shadow damage to all other enemies near them.",
                        "powerCost": "",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 194662,
                        "name": "Rapid Decomposition",
                        "icon": "ability_deathknight_deathsiphon2",
                        "description": "Your Death and Decay deals damage 50% more often, and while in your Death and Decay you generate 15% more Runic Power.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 207060,
                        "name": "Freezing Fog",
                        "icon": "spell_frost_arcticwinds",
                        "description": "Howling Blast and Frost Fever deal 25% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 212744,
                        "name": "Soulgorge",
                        "icon": "ability_ironmaidens_whirlofblood",
                        "description": "Consume your Blood Plagues within 30 yards, dealing 22,125 Shadow damage to each infected enemy, and empowering you for 24 sec with up to 15% Rune regeneration per plague. Plagues closer to expiration grant more Rune regeneration.\n\n\n\nPassive: Blood Boil no longer applies Blood Plague.",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 194917,
                        "name": "Pestilent Pustules",
                        "icon": "spell_yorsahj_bloodboil_purpleoil",
                        "description": "Every 6 Festering Wounds you burst, you gain 1 Rune.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 194909,
                        "name": "Frozen Pulse",
                        "icon": "inv_misc_permafrostshard",
                        "description": "While you have fewer than 2 full Runes, your auto attacks radiate intense cold, inflicting 14,416 Frost damage on all nearby enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 57330,
                        "name": "Horn of Winter",
                        "icon": "inv_misc_horn_02",
                        "description": "Blow the Horn of Winter, gaining 2 runes and generating 10 Runic Power.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 211078,
                        "name": "Spectral Deflection",
                        "subtext": "Passive Talent",
                        "icon": "spell_deathknight_spelldeflection",
                        "description": "Attacks that deal more than 25% of your maximum health will consume a second Bone Shield charge to further reduce the damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 194918,
                        "name": "Blighted Rune Weapon",
                        "icon": "spell_deathknight_plaguestrike",
                        "description": "Your next 4 auto attacks infect your target with 2 Festering Wounds.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 207289,
                        "name": "Unholy Frenzy",
                        "icon": "spell_shadow_unholyfrenzy",
                        "description": "When a Festering Wound bursts, you gain 100% increased attack speed for 2 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 219786,
                        "name": "Ossuary",
                        "icon": "ability_deathknight_brittlebones",
                        "description": "While you have at least 5 Bone Shield charges, the cost of Death Strike is reduced by 5 Runic Power.\n\n\n\nAdditionally, your maximum Runic Power is increased by 10.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 207126,
                        "name": "Icecap",
                        "icon": "inv_misc_herb_icecap",
                        "description": "Your Frost Strike and Obliterate critical strikes reduce the remaining cooldown of Pillar of Frost by 1.0 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 207305,
                        "name": "Castigator",
                        "icon": "spell_shadow_fumble",
                        "description": "Each Festering Strike critical strike applies 2 additional Festering Wounds.\n\n\n\nEach Scourge Strike critical strike bursts 1 additional Festering Wound.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 207127,
                        "name": "Hungering Rune Weapon",
                        "icon": "ability_deathknight_hungeringruneblade",
                        "description": "Empower your rune weapon, gaining 1 Rune and 5 Runic Power instantly and every 1.5 sec for 12 sec.",
                        "castTime": "Instant",
                        "cooldown": "1 sec cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 221699,
                        "name": "Blood Tap",
                        "icon": "spell_deathknight_bloodtap",
                        "description": "Consume shadowy essence.\n\n\n\nGenerates 1 Rune.\n\n\n\nMaximum 2 charges. Recharge time reduced by 1 sec whenever a Bone Shield charge is consumed.",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 207142,
                        "name": "Avalanche",
                        "icon": "spell_frost_icestorm",
                        "description": "While Pillar of Frost is active, your melee critical strikes cause jagged icicles to fall on your nearby enemies, dealing 10,921 Frost damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 207311,
                        "name": "Clawing Shadows",
                        "icon": "warlock_curse_shadow",
                        "description": "Deals 33,425 Shadow damage and causes 1 Festering Wound to burst.",
                        "range": "30 yd range",
                        "powerCost": "1 Death",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 205727,
                        "name": "Anti-Magic Barrier",
                        "icon": "spell_shadow_antimagicshell",
                        "description": "Anti-Magic Shell also increases your maximum health by 25% for 10 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 207313,
                        "name": "Sludge Belcher",
                        "icon": "achievement_boss_patchwerk",
                        "description": "Raise Dead now summons an abomination instead of a ghoul, with improved innate abilities.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 207161,
                        "name": "Abomination's Might",
                        "icon": "spell_deathknight_icetouch",
                        "description": "Obliterate critical strikes have a chance to drive lesser enemies to the ground, stunning them for 2 sec. Players are Dazed for 5 sec instead.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 206940,
                        "name": "Mark of Blood",
                        "icon": "ability_hunter_rapidkilling",
                        "description": "Places a Mark of Blood on an enemy for 25 sec. The enemy's damaging auto attacks will also heal their victim for 2% of maximum health.",
                        "range": "15 yd range",
                        "powerCost": "",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 108194,
                        "name": "Asphyxiate",
                        "icon": "ability_deathknight_asphixiate",
                        "description": "Lifts the enemy target off the ground, crushing their throat with dark energy and stunning them for 5 sec.",
                        "range": "20 yd range",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 207167,
                        "name": "Blinding Sleet",
                        "icon": "spell_frost_chillingblast",
                        "description": "Targets in a cone in front of you are blinded, causing them to wander disoriented for 4 sec. Damage may cancel the effect.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 205723,
                        "name": "Red Thirst",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "Spending Runic Power will decrease the remaining cooldown on Vampiric Blood by 1 sec per 6 Runic Power.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 207170,
                        "name": "Winter is Coming",
                        "icon": "inv_wolfdraenormountfrost",
                        "description": "Enemies struck 5 times by Remorseless Winter while your Pillar of Frost is active are stunned for 4 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 219809,
                        "name": "Tombstone",
                        "icon": "ability_fiegndead",
                        "description": "Consume all Bone Shield charges. For each charge consumed, you gain 3 Runic Power and absorb damage equal to 3% of your maximum health for 8 sec.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 207316,
                        "name": "Debilitating Infestation",
                        "icon": "spell_deathknight_necroticplague",
                        "description": "Outbreak reduces the movement speed of all affected enemies by 50% for 3 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 207321,
                        "name": "Spell Eater",
                        "icon": "ability_creature_cursed_03",
                        "description": "Your Anti-Magic Shell is 20% larger and lasts 5 sec longer.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 206970,
                        "name": "Tightening Grasp",
                        "icon": "spell_shadow_chilltouch",
                        "description": "Reduces the cooldown on Gorefiend's Grasp by 60 sec, and your Death and Decay also reduces the movement speed of enemies within its radius by 70%.",
                        "castTime": "Passive",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 207188,
                        "name": "Volatile Shielding",
                        "icon": "ability_mage_shattershield",
                        "description": "Your Anti-Magic Shell turns your enemies' pathetic magic against them, absorbing 35% more damage, but generating no Runic Power. When it expires, 25% of all damage absorbed is dealt as Arcane damage divided among nearby enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 207200,
                        "name": "Permafrost",
                        "icon": "achievement_zone_frostfire",
                        "description": "When you deal damage with auto attacks, gain an absorb shield equal to 30% of the damage dealt.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 207319,
                        "name": "Corpse Shield",
                        "icon": "inv_pet_ghoul",
                        "description": "For the next 10 sec, 90% of all damage you take is transferred to your ghoul.\n\n\n\nIf your ghoul is slain while this spell is active, it cannot be resummoned for 30 seconds.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 206960,
                        "name": "Tremble Before Me",
                        "icon": "spell_shadow_auraofdarkness",
                        "description": "Enemies damaged by your Death and Decay have a chance to cower in place for 3 sec, but cannot suffer from this effect more than once per 10 sec. Damage may cancel the effect.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 212765,
                        "name": "White Walker",
                        "icon": "ability_deathknight_icygrip",
                        "description": "You take 20% reduced damage while Wraith Walk is active. When you enter or leave Wraith Walk, all nearby enemies are slowed by 50% for 3 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 219779,
                        "name": "March of the Damned",
                        "icon": "spell_shadow_demonicempathy",
                        "description": "Wraith Walk lasts 50% longer and breaks stun, snare, and root effects when cast.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 212763,
                        "name": "Lingering Apparition",
                        "icon": "spell_holy_senseundead",
                        "description": "You move 30% faster during Wraith Walk, and its cooldown is reduced by 15 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 206967,
                        "name": "Will of the Necropolis",
                        "subtext": "Passive Talent",
                        "icon": "achievement_boss_kelthuzad_01",
                        "description": "Damage taken below 35% Health is reduced by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 207230,
                        "name": "Frostscythe",
                        "icon": "inv_misc_2h_farmscythe_a_01",
                        "description": "A sweeping attack that strikes all enemies in front of you for 34,709 Frost damage. This attack benefits from Killing Machine. Critical strikes with Frostscythe deal 4 times normal damage.",
                        "range": "8 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 198943,
                        "name": "Shadow Infusion",
                        "icon": "spell_shadow_requiem",
                        "description": "While your ghoul is not transformed, Death Coil will also reduce the remaining cooldown of Dark Transformation by 5 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 194679,
                        "name": "Rune Tap",
                        "icon": "spell_deathknight_runetap",
                        "description": "Consume a Rune to reduce all damage taken by 25% for 3 sec.",
                        "powerCost": "60 Runic Power",
                        "castTime": "Instant",
                        "cooldown": "1.5 sec cooldown"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 207346,
                        "name": "Necrosis",
                        "icon": "inv_weapon_shortblade_60",
                        "description": "Dealing damage with Death Coil causes your next Scourge Strike to deal 35% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 207104,
                        "name": "Runic Attenuation",
                        "icon": "boss_odunrunes_blue",
                        "description": "Auto attacks generate 1 Runic Power.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 206974,
                        "name": "Foul Bulwark",
                        "icon": "inv_armor_shield_naxxramas_d_02",
                        "description": "Each charge of Bone Shield increases your maximum health by 2%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 194912,
                        "name": "Gathering Storm",
                        "icon": "spell_frost_iceshards",
                        "description": "Each Rune spent during Remorseless Winter increases its damage by 10%, and extends it by 0.5 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 207272,
                        "name": "Infected Claws",
                        "icon": "spell_deathknight_thrash_ghoul",
                        "description": "Your ghoul's Claw attack has a 35% chance to cause a Festering Wound on the target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 207256,
                        "name": "Obliteration",
                        "icon": "inv_axe_114",
                        "description": "For the next 8 sec, every Frost Strike hit triggers Killing Machine, and Obliterate costs 1 less Rune.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 194844,
                        "name": "Bonestorm",
                        "icon": "ability_deathknight_boneshield",
                        "description": "A whirl of bone and gore batters nearby enemies every 1 sec, dealing 25,314 Shadow damage every 1 sec, and healing you for 1% of your maximum health every time it deals damage. Lasts 1 sec per 10 Runic Power spent.",
                        "powerCost": "20 Runic Power",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 207349,
                        "name": "Dark Arbiter",
                        "icon": "achievement_boss_svalasorrowgrave",
                        "description": "Summon a Val'kyr to attack the target for 15 sec. The Val'kyr will gain 1% increased damage for every 1 Runic Power you spend.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 152280,
                        "name": "Defile",
                        "icon": "spell_deathknight_defile",
                        "description": "Defiles the ground targeted by the Death Knight for 10 sec. Every 1 sec, if there are any enemies standing in the Defile, it deals 8,729 Shadowfrost damage to them and grows in radius, and increases your Mastery by 200, stacking up to 10 times. While you remain within Defile, your Scourge Strike will hit all enemies near the target.",
                        "range": "30 yd range",
                        "powerCost": "10 Runic Power",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 152279,
                        "name": "Breath of Sindragosa",
                        "icon": "spell_deathknight_breathofsindragosa",
                        "description": "Continuously deal 38,223 Shadowfrost damage every 1 sec to enemies in a cone in front of you. Deals reduced damage to secondary targets. You will continue breathing until your Runic Power is exhausted or you cancel the effect.",
                        "powerCost": "",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 206977,
                        "name": "Blood Mirror",
                        "icon": "inv_misc_gem_bloodstone_01",
                        "description": "Afflict an enemy with Blood Mirror for 10 sec.  While active, 20% of any damage dealt to you is redirected to the target.",
                        "range": "Melee Range",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 194913,
                        "name": "Glacial Advance",
                        "icon": "ability_hunter_glacialtrap",
                        "description": "Summon glacial spikes from the ground that advance forward, each dealing 81,904 Frost damage to enemies near their eruption point.",
                        "powerCost": "",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-frost",
                        "icon": "spell_deathknight_frostpresence",
                        "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 114556,
                        "name": "Purgatory",
                        "icon": "inv_misc_shadowegg",
                        "description": "An unholy pact that prevents fatal damage, instead absorbing incoming healing equal to the damage prevented, lasting 3 sec.\n\n\n\nIf any healing absorption remains when this effect expires, you will die. This effect may only occur every 3 min.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Blood",
                        "role": "TANK",
                        "backgroundImage": "bg-deathknight-blood",
                        "icon": "spell_deathknight_bloodpresence",
                        "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 130736,
                        "name": "Soul Reaper",
                        "icon": "ability_deathknight_soulreaper",
                        "description": "Strike an enemy's soul for 89,986 Shadow damage, afflicting them with Soul Reaper for 5 sec.\n\n\n\nBursting a Festering Wound on an enemy afflicted by Soul Reaper grants 7% Haste for 15 sec, stacking up to 3 times.",
                        "range": "Melee Range",
                        "powerCost": "1 Unholy",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Unholy",
                        "role": "DPS",
                        "backgroundImage": "bg-deathknight-unholy",
                        "icon": "spell_deathknight_unholypresence",
                        "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
                        "order": 2
                    }
                }]
            ]
        ],
        "class": "death-knight",
        "specs": [{
            "name": "Blood",
            "role": "TANK",
            "backgroundImage": "bg-deathknight-blood",
            "icon": "spell_deathknight_bloodpresence",
            "description": "A dark guardian who manipulates and corrupts life energy to sustain herself in the face of an enemy onslaught.",
            "order": 0
        }, {
            "name": "Frost",
            "role": "DPS",
            "backgroundImage": "bg-deathknight-frost",
            "icon": "spell_deathknight_frostpresence",
            "description": "An icy harbinger of doom, channeling runic power and delivering vicious weapon strikes.",
            "order": 1
        }, {
            "name": "Unholy",
            "role": "DPS",
            "backgroundImage": "bg-deathknight-unholy",
            "icon": "spell_deathknight_unholypresence",
            "description": "A master of death and decay, spreading infection and controlling undead minions to do his bidding.",
            "order": 2
        }]
    },
    "7": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 201898,
                        "name": "Windsong",
                        "icon": "ability_skyreach_wind_wall",
                        "description": "Lashes your enemy for 24,025 Nature damage, and enhances your weapons with wind, increasing your attack speed by 35% for 20 sec.",
                        "range": "10 yd range",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 200071,
                        "name": "Undulation",
                        "icon": "spell_nature_healingwavelesser",
                        "description": "Every third Healing Wave or Healing Surge you cast heals for an additional 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 201909,
                        "name": "Path of Flame",
                        "icon": "spell_mage_flameorb",
                        "description": "Lava Burst deals 5% more damage and causes Flame Shock to spread from the target to a nearby enemy.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 170374,
                        "name": "Earthen Rage",
                        "icon": "ability_earthen_pillar",
                        "description": "Your damaging spells incite the earth around you to come to your aid for 6 sec, repeatedly dealing 3,003 Nature damage to your most recently attacked target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 201900,
                        "name": "Hot Hand",
                        "icon": "spell_fire_playingwithfire",
                        "description": "Melee attacks with Flametongue active have a chance to make your next Lava Lash cost no Maelstrom and deal 100% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 73685,
                        "name": "Unleash Life",
                        "icon": "spell_shaman_unleashweapon_life",
                        "description": "Unleashes elemental forces of Life, healing a friendly target for 19,520 and increasing the effect of the Shaman's next direct heal by 45%.",
                        "powerCost": "5% of base mana",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 201897,
                        "name": "Boulderfist",
                        "icon": "ability_earthenfury_giftofearth",
                        "description": "Slams your target with the power of stone, dealing 54,604 Nature damage and enhancing your weapons for 10 sec, increasing your critical strike chance by 5% and all damage you deal by 5%.\n\n\n\nGenerates 25 Maelstrom.",
                        "range": "10 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 200072,
                        "name": "Torrent",
                        "icon": "spell_nature_riptide",
                        "description": "Increases the initial heal from Riptide by 30%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 210643,
                        "name": "Totem Mastery",
                        "icon": "spell_nature_wrathofair_totem",
                        "description": "Summons four totems that increase your combat capabilities for 2 min.\n\n\n\nResonance Totem\n\nGenerates 1 Maelstrom every 1 sec.\n\n\n\nStorm Totem\n\nIncreases the chance for Lightning Bolt and Chain Lightning to trigger Elemental Overload by 10%.\n\n\n\nEmber Totem\n\nIncreases Flame Shock damage over time by 10%.\n\n\n\nTailwind Totem\n\nIncreases your haste by 2%.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 192063,
                        "name": "Gust of Wind",
                        "icon": "ability_skyreach_four_wind",
                        "description": "A gust of wind hurls you forward.",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 215864,
                        "name": "Rainfall",
                        "icon": "spell_nature_giftofthewaterspirit",
                        "description": "Blankets the target area in healing rain, restoring 15,015 health to up to 6 allies over 10 sec. Stormstrike and Lava Lash extend the duration of Rainfall by 3 sec, up to a maximum of 30 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 108281,
                        "name": "Ancestral Guidance",
                        "icon": "ability_shaman_ancestralguidance",
                        "description": "For the next 10 sec, 20% of your damage and healing is converted to healing on up to 3 nearby injured party or raid members.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 192088,
                        "name": "Graceful Spirit",
                        "icon": "spell_shaman_spectraltransformation",
                        "description": "Reduces the cooldown of Spiritwalker's Grace by 60 sec and increases your movement speed by 20% while it is active, and increases your movement speed in Ghost Wolf by an additional 10%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 196884,
                        "name": "Feral Lunge",
                        "icon": "spell_beastmaster_wolf",
                        "description": "Lunge at your enemy as a ghostly wolf, biting them to deal 43,682 Physical damage.",
                        "range": "8-25 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 192077,
                        "name": "Wind Rush Totem",
                        "icon": "ability_shaman_windwalktotem",
                        "description": "Summons a totem at the target location for 15 sec, continually granting all allies who pass within 10 yards 60% increased movement speed for 5 sec.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 192058,
                        "name": "Lightning Surge Totem",
                        "icon": "spell_nature_brilliance",
                        "description": "Summons a totem at the target location that gathers electrical energy from the surrounding air and then explodes after 2 sec to stun all enemies within 8 yards for 5 sec.",
                        "range": "35 yd range",
                        "powerCost": "10% of base mana",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 51485,
                        "name": "Earthgrab Totem",
                        "icon": "spell_nature_stranglevines",
                        "description": "Summons a totem at the target location for 20 sec. The totem pulses every 2 sec, rooting all enemies within 10 yards for 5 sec. Enemies previously rooted by the totem instead suffer 50% movement speed reduction.",
                        "range": "35 yd range",
                        "powerCost": "10% of base mana",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 196932,
                        "name": "Voodoo Totem",
                        "icon": "spell_totem_wardofdraining",
                        "description": "Summons a totem at the target location for 10 sec. The totem Hexes all enemies within 8 yds into frogs which are incapacitated and unable to attack or cast spells. Damage or leaving the area will interrupt the effect.",
                        "range": "35 yd range",
                        "powerCost": "10% of base mana",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 117014,
                        "name": "Elemental Blast",
                        "icon": "shaman_talent_elementalblast",
                        "description": "Harnesses the raw power of the elements, dealing 31,532 Elemental damage and increasing your Critical Strike, Haste, or Mastery by 1,200 for 10 sec.",
                        "range": "40 yd range",
                        "castTime": "2 sec cast",
                        "cooldown": "12 sec cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 197464,
                        "name": "Crashing Waves",
                        "icon": "spell_frost_summonwaterelemental",
                        "description": "Riptide grants an additional stack of Tidal Waves.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 192106,
                        "name": "Lightning Shield",
                        "icon": "spell_nature_lightningshield",
                        "description": "Surround yourself with a shield of lighting for 1 hour which has a chance to deal 13,105 Nature damage when you deal or take melee damage.",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 192087,
                        "name": "Ancestral Swiftness",
                        "icon": "spell_shaman_elementaloath",
                        "description": "Increases haste by 10%.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 108281,
                        "name": "Ancestral Guidance",
                        "icon": "ability_shaman_ancestralguidance",
                        "description": "For the next 10 sec, 20% of your damage and healing is converted to healing on up to 3 nearby injured party or raid members.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 108283,
                        "name": "Echo of the Elements",
                        "icon": "ability_shaman_echooftheelements",
                        "description": "Riptide, Healing Stream Totem, and Lava Burst now have 2 charges. Other effects that reset their remaining cooldown will instead grant 1 charge.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 210853,
                        "name": "Hailstorm",
                        "icon": "spell_frost_frostbrand",
                        "description": "Frostbrand now also enhances your weapon's damage, causing each of your weapon attacks to also deal 8,998 Frost damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 200076,
                        "name": "Deluge",
                        "icon": "ability_shawaterelemental_reform",
                        "description": "Chain Heal heals for an additional 20% on targets within your Healing Rain or affected by your Riptide.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 192235,
                        "name": "Elemental Fusion",
                        "icon": "spell_shaman_shockinglava",
                        "description": "Flame Shock has a 5% increased chance to trigger Lava Surge.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 192234,
                        "name": "Tempest",
                        "icon": "inv_misc_herb_stormvine",
                        "description": "Stormbringer now affects the next 2 Stormstrikes.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 207399,
                        "name": "Ancestral Protection Totem",
                        "icon": "spell_nature_reincarnation",
                        "description": "Summons a totem at the target location for 30 sec. All allies within 20 yards of the totem gain 10% increased health. If an ally dies, the totem will be consumed to allow them to Reincarnate with 20% health and mana.\n\n\n\nCannot reincarnate an ally who dies to massive damage.",
                        "range": "40 yd range",
                        "powerCost": "11% of base mana",
                        "castTime": "Instant",
                        "cooldown": "5 min cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 210727,
                        "name": "Overcharge",
                        "icon": "spell_nature_callstorm",
                        "description": "Lightning Bolt now consumes up to 45 Maelstrom for up to 1,500% increased damage, but has a 9 sec cooldown.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 117013,
                        "name": "Primal Elementalist",
                        "icon": "shaman_talent_primalelementalist",
                        "description": "Your Earth, Fire, and Storm Elementals are drawn from primal elementals 80% more powerful than regular elementals, with additional abilities, and you gain direct control over them.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 198838,
                        "name": "Earthen Shield Totem",
                        "icon": "spell_nature_stoneskintotem",
                        "description": "Summons a totem with 1,589,040 health for 15 sec. 6,006 damage from each attack against allies within 10 yards of the totem is redirected to the totem.",
                        "range": "40 yd range",
                        "powerCost": "11% of base mana",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 210714,
                        "name": "Icefury",
                        "icon": "spell_frost_iceshard",
                        "description": "Hurls frigid ice at the target, dealing 10,812 Frost damage and causing your next 4 Frost Shocks to deal 400% increased damage.\n\n\n\nGenerates 24 Maelstom.",
                        "range": "40 yd range",
                        "castTime": "2 sec cast",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 210731,
                        "name": "Empowered Stormlash",
                        "icon": "spell_lightning_lightningbolt01",
                        "description": "Stormlash now spreads to 1 additional target and deals 35% additional damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 207401,
                        "name": "Ancestral Vigor",
                        "icon": "spell_shaman_blessingoftheeternals",
                        "description": "Targets you heal with Healing Wave, Healing Surge, Chain Heal, or Riptide's initial heal gain 10% increased health for 10 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 197467,
                        "name": "Bottomless Depths",
                        "icon": "ability_shawaterelemental_swirl",
                        "description": "Resurgence always triggers when you heal a target below 60% health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 192246,
                        "name": "Crashing Storm",
                        "icon": "spell_nature_unrelentingstorm",
                        "description": "Crash Lightning also electrifies the ground, leaving an electrical field behind which damages enemies within it for 18,354 Nature damage over 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 16166,
                        "name": "Elemental Mastery",
                        "icon": "spell_nature_wispheal",
                        "description": "Elemental forces empower you with 20% haste for 20 sec.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 192249,
                        "name": "Storm Elemental",
                        "icon": "spell_shaman_measuredinsight",
                        "description": "Calls forth a Greater Storm Elemental to hurl gusts of wind that damage the Shaman's enemies and generate Maelstrom for the Shaman for 1 min.",
                        "castTime": "Instant",
                        "cooldown": "5 min cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 157153,
                        "name": "Cloudburst Totem",
                        "icon": "ability_shaman_condensationtotem",
                        "description": "Summons a totem at your feet for 15 sec that collects power from all of your healing spells. When the totem expires or dies, the stored power is released, healing all injured allies within 40 yards for 25% of all healing done while it was active, divided evenly among targets.\n\n\n\nCasting this spell a second time recalls the totem and releases the healing.",
                        "powerCost": "8.6% of base mana",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 197211,
                        "name": "Fury of Air",
                        "icon": "ability_ironmaidens_swirlingvortex",
                        "description": "Creates a vortex of wind 8 yards around you, dealing 6,552 Nature damage every 1 sec to enemies caught in the storm, and slowing them by 30% for 3 sec.",
                        "powerCost": "5 Maelstrom",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 197214,
                        "name": "Sundering",
                        "icon": "ability_rhyolith_lavapool",
                        "description": "Shatters a line of earth in front of you with your main hand weapon, causing 218,411 Physical damage and knocking enemies to the side.",
                        "powerCost": "60 Maelstrom",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 108283,
                        "name": "Echo of the Elements",
                        "icon": "ability_shaman_echooftheelements",
                        "description": "Riptide, Healing Stream Totem, and Lava Burst now have 2 charges. Other effects that reset their remaining cooldown will instead grant 1 charge.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 210707,
                        "name": "Aftershock",
                        "icon": "spell_nature_stormreach",
                        "description": "Your spells refund 25% of all Maelstrom spent on them.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 114052,
                        "name": "Ascendance",
                        "icon": "spell_fire_elementaldevastation",
                        "description": "Transform into a Water Ascendant for 15 sec, causing all healing you deal to be duplicated and distributed evenly among nearby allies.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 114051,
                        "name": "Ascendance",
                        "icon": "spell_fire_elementaldevastation",
                        "description": "Transform into an Air Ascendant for 15 sec, generating 10 Maelstrom per second, and transforming your auto attack and Stormstrike into Wind attacks, which bypass armor and have a 30 yd range.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 114050,
                        "name": "Ascendance",
                        "icon": "spell_fire_elementaldevastation",
                        "description": "Transform into a Flame Ascendant for 15 sec, replacing Chain Lightning with Lava Beam, removing the cooldown on Lava Burst, and increasing the damage of Lava Burst by an amount equal to your critical strike chance.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 197992,
                        "name": "Landslide",
                        "icon": "inv_ore_blackrock_nugget",
                        "description": "Rockbiter now also enhances your weapon, increasing your Agility by 8% for 10 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 210689,
                        "name": "Lightning Rod",
                        "icon": "inv_rod_enchantedcobalt",
                        "description": "Your Lightning Bolt and Chain Lightning have a 30% chance to make the primary target a Lightning Rod for 10 sec. Lightning Rods take 40% of all damage you deal with Lightning Bolt and Chain Lightning.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 197995,
                        "name": "Wellspring",
                        "icon": "ability_shawaterelemental_split",
                        "description": "Creates a surge of water that flows forward, healing friendly targets in a wide arc in front of you for 22,523.",
                        "range": "30 yd range",
                        "powerCost": "35% of base mana",
                        "castTime": "1.5 sec cast",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 192222,
                        "name": "Liquid Magma Totem",
                        "icon": "spell_shaman_spewlava",
                        "description": "Summons a totem at the target location for 15 sec that hurls liquid magma at a random nearby target every 1 sec, dealing 4,806 Fire damage to all enemies within 8 yards.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Elemental",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-elemental",
                        "icon": "spell_nature_lightning",
                        "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 188089,
                        "name": "Earthen Spike",
                        "icon": "ability_earthen_pillar",
                        "description": "Summons an Earthen Spike under an enemy, dealing 174,728 Physical damage and increasing Physical and Nature damage you deal to the target by 15% for 10 sec.",
                        "range": "10 yd range",
                        "powerCost": "30 Maelstrom",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Enhancement",
                        "role": "DPS",
                        "backgroundImage": "bg-shaman-enhancement",
                        "icon": "spell_shaman_improvedstormstrike",
                        "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 157154,
                        "name": "High Tide",
                        "icon": "spell_shaman_hightide",
                        "description": "Chain Heal bounces to 1 additional target, and its falloff with each bounce is reduced by half.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-shaman-restoration",
                        "icon": "spell_nature_magicimmunity",
                        "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
                        "order": 2
                    }
                }]
            ]
        ],
        "class": "shaman",
        "specs": [{
            "name": "Elemental",
            "role": "DPS",
            "backgroundImage": "bg-shaman-elemental",
            "icon": "spell_nature_lightning",
            "description": "A spellcaster who harnesses the destructive forces of nature and the elements.",
            "order": 0
        }, {
            "name": "Enhancement",
            "role": "DPS",
            "backgroundImage": "bg-shaman-enhancement",
            "icon": "spell_shaman_improvedstormstrike",
            "description": "A totemic warrior who strikes foes with weapons imbued with elemental power.",
            "order": 1
        }, {
            "name": "Restoration",
            "role": "HEALING",
            "backgroundImage": "bg-shaman-restoration",
            "icon": "spell_nature_magicimmunity",
            "description": "A healer who calls upon ancestral spirits and the cleansing power of water to mend allies' wounds.",
            "order": 2
        }]
    },
    "8": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 205020,
                        "name": "Pyromaniac",
                        "icon": "inv_misc_volatilefire",
                        "description": "Casting Pyroblast or Flamestrike while Hot Streak is active has a 8% chance to instantly reactivate Hot Streak.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 205021,
                        "name": "Ray of Frost",
                        "icon": "spell_frost_chillingblast",
                        "description": "For the next 10 sec, you can channel a beam of icy power at an enemy, slowing movement by 50% and dealing 11,670 Frost damage every 1 sec. Each time Ray of Frost deals damage, its damage increases by 20%.",
                        "range": "40 yd range",
                        "castTime": "Channeled",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 205022,
                        "name": "Arcane Familiar",
                        "icon": "ability_socererking_arcanemines",
                        "description": "Summon a Familiar that attacks your enemies and increases your maximum mana by 10%.  Lasts 1 hour.",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 205023,
                        "name": "Conflagration",
                        "icon": "spell_shaman_firenova",
                        "description": "Fireball also applies Conflagration to the target, dealing an additional 1,200 Fire damage over 8 sec.\n\n\n\nEnemies affected by either Conflagration or Ignite have a 10% chance to flare up and deal 2,403 Fire damage to nearby enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 205025,
                        "name": "Presence of Mind",
                        "icon": "spell_nature_enchantarmor",
                        "description": "Causes your next 2 Arcane Blasts to be instant cast.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 205024,
                        "name": "Lonely Winter",
                        "icon": "achievement_dungeon_frozenthrone",
                        "description": "You can no longer summon your Water Elemental, but Frostbolt, Ice Lance, Flurry, and Frozen Orb deal 25% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 205035,
                        "name": "Words of Power",
                        "icon": "spell_arcane_rune",
                        "description": "Grants 1% increased chance to trigger Arcane Missiles per 20% of your mana you have unspent.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 205027,
                        "name": "Bone Chilling",
                        "icon": "ability_mage_chilledtothebone",
                        "description": "Whenever you attempt to chill a target, you gain Bone Chilling, increasing all Frost damage you deal by 0.5% for 8 sec, stacking up to 12 times.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 205026,
                        "name": "Firestarter",
                        "icon": "spell_fire_fire",
                        "description": "Your Fireball spell always deals a critical strike when the target is above 85% health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 212653,
                        "name": "Shimmer",
                        "icon": "spell_arcane_massdispel",
                        "description": "Teleports you 20 yards forward, unless something is in the way. Unaffected by the global cooldown and castable while casting. Max 2 charges.",
                        "powerCost": "2% of base mana",
                        "castTime": "Instant",
                        "cooldown": "0.5 sec cooldown"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 86949,
                        "name": "Cauterize",
                        "icon": "spell_fire_rune",
                        "description": "Fatal damage instead brings you to 35% health and then burns you for 28% of your maximum health over 6 sec. While burning, movement slowing effects are suppressed and your movement speed is increased by 150%. This effect cannot occur more than once every 2 min.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 11958,
                        "name": "Cold Snap",
                        "icon": "spell_frost_wizardmark",
                        "description": "Ice Block now has 2 charges and also heals you for 3% of your maximum health every 1 sec.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 55342,
                        "name": "Mirror Image",
                        "icon": "spell_magic_lesserinvisibilty",
                        "description": "Creates 3 copies of you nearby, which cast spells and attack your enemies. Lasts 40 sec.",
                        "powerCost": "2% of base mana",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 116011,
                        "name": "Rune of Power",
                        "icon": "spell_mage_runeofpower",
                        "description": "Places a Rune of Power on the ground for 10 sec which increases your spell damage by 50% while you stand within 8 yds. Max 2 charges.",
                        "range": "30 yd range",
                        "castTime": "1.5 sec cast",
                        "cooldown": "10 sec cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 1463,
                        "name": "Incanter's Flow",
                        "icon": "ability_mage_incantersabsorbtion",
                        "description": "Magical energy flows through you while in combat, building up to 20% increased damage and then diminishing down to 4% increased damage, cycling every 10 sec.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 157997,
                        "name": "Ice Nova",
                        "icon": "spell_mage_icenova",
                        "description": "Causes a whirl of icy wind around the target enemy or ally, dealing 27,028 Frost damage to all enemies within 8 yards, and freezing them in place for 2 sec. A primary enemy target will take 100% increased damage.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "25 sec cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 157980,
                        "name": "Supernova",
                        "icon": "spell_mage_supernova",
                        "description": "Pulses arcane energy around the target enemy or ally, dealing 11,412 Arcane damage to all enemies within 8 yards, and knocking them upward. A primary enemy target will take 100% increased damage.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "25 sec cooldown"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 157981,
                        "name": "Blast Wave",
                        "icon": "spell_holy_excorcism_02",
                        "description": "Causes an explosion around the target enemy or ally, dealing 12,013 Fire damage to all enemies within 8 yards, and reducing movement speed by 70% for 4 sec. A primary enemy target will take 100% increased damage.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "25 sec cooldown"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 205032,
                        "name": "Charged Up",
                        "icon": "ability_thunderking_overcharge",
                        "description": "Immediately grants 4 Arcane Charges.",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 205030,
                        "name": "Frozen Touch",
                        "icon": "ability_mage_coldasice",
                        "description": "Immediately generates 2 charges of Fingers of Frost.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 205029,
                        "name": "Flame On",
                        "icon": "inv_helm_circlet_firelands_d_01",
                        "description": "Immediately grants 2 charges of Fire Blast.",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 205033,
                        "name": "Controlled Burn",
                        "icon": "inv_trinket_firelands_02",
                        "description": "When you gain Heating Up, you have a 10% chance to instantly activate Hot Streak.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 205028,
                        "name": "Resonance",
                        "icon": "spell_arcane_arcane01",
                        "description": "Arcane Barrage deals 25% increased damage per target it hits.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 56377,
                        "name": "Splitting Ice",
                        "icon": "spell_frost_iceshards",
                        "description": "Your Ice Lance and Icicles now deal 5% increased damage, and hit a second nearby target for 80% of their damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 108839,
                        "name": "Ice Floes",
                        "icon": "spell_mage_iceflows",
                        "description": "Makes your next Mage spell with a cast time shorter than 10 sec castable while moving. Unaffected by the global cooldown and castable while casting. Max 3 charges.",
                        "castTime": "Instant"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 113724,
                        "name": "Ring of Frost",
                        "icon": "spell_frost_ringoffrost",
                        "description": "Summons a Ring of Frost for 10 sec at the target location. Enemies entering the ring are incapacitated for 10 sec. Limit 10 targets.",
                        "range": "30 yd range",
                        "powerCost": "2% of base mana",
                        "castTime": "2 sec cast",
                        "cooldown": "45 sec cooldown"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 205036,
                        "name": "Ice Ward",
                        "icon": "spell_frost_frostward",
                        "description": "Frost Nova now has 2 charges.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 112948,
                        "name": "Frost Bomb",
                        "icon": "spell_mage_frostbomb",
                        "description": "Places a Frost Bomb on the target for 12 sec. Limit 1 target. Your Ice Lances that benefit from Shatter will trigger the release of a wave of freezing ice, dealing 9,459 Frost damage to the target and 5,910 Frost damage to all other enemies within 10 yards.",
                        "range": "40 yd range",
                        "powerCost": "1.25% of base mana",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 44457,
                        "name": "Living Bomb",
                        "icon": "ability_mage_livingbomb",
                        "description": "The target becomes a Living Bomb, taking 6,012 Fire damage over 3.6 sec, and then exploding to deal an additional 4,806 Fire damage to the target and all other enemies within 10 yards.\n\n\n\nOther enemies hit by this explosion also become a Living Bomb, but this effect cannot spread further.",
                        "range": "40 yd range",
                        "powerCost": "1.5% of base mana",
                        "castTime": "Instant",
                        "cooldown": "12 sec cooldown"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 114923,
                        "name": "Nether Tempest",
                        "icon": "spell_mage_nethertempest",
                        "description": "Places a Nether Tempest on the target which deals 3,972 Arcane damage over 12 sec to the target and 3,972 to all enemies within 10 yards. Limit 1 target.\n\n\n\nDamage increased by 60% per Arcane Charge.",
                        "range": "40 yd range",
                        "powerCost": "1.5% of base mana",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 157976,
                        "name": "Unstable Magic",
                        "icon": "spell_mage_unstablemagic",
                        "description": "Frostbolt has a 25% chance to explode on impact, dealing 50% additional damage to the target and all other enemies within 8 yds.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 205038,
                        "name": "Arctic Gale",
                        "icon": "spell_frost_arcticwinds",
                        "description": "Increases Blizzard's damage by 30% and its area of effect by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 205039,
                        "name": "Erosion",
                        "icon": "ability_mage_missilebarrage",
                        "description": "Your attacks erode the target's resistances, increasing all damage the target takes from your Arcane spells by 1%, stacking up to 8 times.  After 3 sec of not taking damage from your spells, this effect decreases by 1% every 1 sec.",
                        "range": "40 yd range",
                        "castTime": "Passive",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 205037,
                        "name": "Flame Patch",
                        "icon": "spell_mage_flameorb",
                        "description": "Flamestrike leaves behind a patch of flames which burns enemies within it for 12,024 Fire damage over 8 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 155147,
                        "name": "Overpowered",
                        "icon": "spell_mage_overpowered",
                        "description": "Casting Arcane Missiles extends Arcane Power by 2 sec.",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 155148,
                        "name": "Kindling",
                        "icon": "spell_mage_kindling",
                        "description": "Your Fireball, Pyroblast, and Fire Blast critical strikes reduce the remaining cooldown on Combustion by 1 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 155149,
                        "name": "Thermal Void",
                        "icon": "spell_mage_thermalvoid",
                        "description": "Your Ice Lances against frozen targets extend your Icy Veins by 2 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 198929,
                        "name": "Cinderstorm",
                        "icon": "spell_fire_flare",
                        "description": "Throws a spread of 6 cinders that travel in an arc, each dealing 3,483 Fire damage to enemies it hits. Damage increased by 30% if the target is affected by your Ignite.",
                        "range": "40 yd range",
                        "powerCost": "1% of base mana",
                        "castTime": "1.5 sec cast",
                        "cooldown": "9 sec cooldown"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 199786,
                        "name": "Glacial Spike",
                        "icon": "spell_frost_frostbolt",
                        "description": "Conjures a massive spike of ice, and merges your current Icicles into it. It impales your target, dealing 45,045 damage plus the damage stored in your Icicles, and freezes the target in place for 4 sec. Damage may interrupt the freeze effect.\n\n\n\nRequires 5 Icicles to cast.\n\n\n\nPassive:\n\nIce Lance no longer launches Icicles.",
                        "range": "40 yd range",
                        "powerCost": "1% of base mana",
                        "castTime": "3 sec cast"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 198923,
                        "name": "Quickening",
                        "icon": "spell_arcane_invocation",
                        "description": "Arcane Blast, Arcane Missiles, and Arcane Explosion also grant 2% Haste for 6 sec, stacking up to 50 times.\n\n\n\nThis effect is cleared when you cast Arcane Barrage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 153595,
                        "name": "Comet Storm",
                        "icon": "spell_mage_cometstorm",
                        "description": "Calls down a series of 7 icy comets on and around the target, each of which deals 6,307 Frost damage to all enemies within 4 yards of its impact.",
                        "range": "40 yd range",
                        "powerCost": "1% of base mana",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Frost",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-frost",
                        "icon": "spell_frost_frostbolt02",
                        "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 153626,
                        "name": "Arcane Orb",
                        "icon": "spell_mage_arcaneorb",
                        "description": "Launches an Arcane Orb forward from your position, traveling up to 40 yards, dealing 5,201 Arcane damage to enemies it passes through.\n\n\n\nGrants 1 Arcane Charge when cast and every time it deals damage.",
                        "range": "40 yd range",
                        "powerCost": "1% of base mana",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Arcane",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-arcane",
                        "icon": "spell_holy_magicalsentry",
                        "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 153561,
                        "name": "Meteor",
                        "icon": "spell_mage_meteor",
                        "description": "Calls down a meteor which lands at the target location after 3 sec, dealing 33,785 Fire damage, split evenly between all targets within 8 yards, and burns the ground, dealing 9,008 Fire damage over 8 sec to all enemies in the area.",
                        "range": "40 yd range",
                        "powerCost": "1% of base mana",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Fire",
                        "role": "DPS",
                        "backgroundImage": "bg-mage-fire",
                        "icon": "spell_fire_firebolt02",
                        "description": "Ignite enemies with balls of fire and combustive flames.",
                        "order": 1
                    }
                }]
            ]
        ],
        "class": "mage",
        "specs": [{
            "name": "Arcane",
            "role": "DPS",
            "backgroundImage": "bg-mage-arcane",
            "icon": "spell_holy_magicalsentry",
            "description": "Manipulate the arcane, destroying enemies with overwhelming power.",
            "order": 0
        }, {
            "name": "Fire",
            "role": "DPS",
            "backgroundImage": "bg-mage-fire",
            "icon": "spell_fire_firebolt02",
            "description": "Ignite enemies with balls of fire and combustive flames.",
            "order": 1
        }, {
            "name": "Frost",
            "role": "DPS",
            "backgroundImage": "bg-mage-frost",
            "icon": "spell_frost_frostbolt02",
            "description": "Freezes enemies in their tracks and shatters them with Frost magic.",
            "order": 2
        }]
    },
    "9": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 196269,
                        "name": "Shadowy Inspiration",
                        "icon": "warlock_curse_shadow",
                        "description": "Demonic Empowerment also causes your next Shadow Bolt to be Instant.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 48181,
                        "name": "Haunt",
                        "icon": "ability_warlock_haunt",
                        "description": "A ghostly soul haunts the target, dealing 48,349 Shadow damage. If the target dies within 15 sec, Haunt's cooldown is reset.",
                        "range": "40 yd range",
                        "powerCost": "5% of base mana",
                        "castTime": "1.5 sec cast",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 196406,
                        "name": "Backdraft",
                        "icon": "ability_warlock_backdraft",
                        "description": "Casting Conflagrate reduces the cast time of Incinerate and Chaos Bolt by 30% for 5 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 196102,
                        "name": "Writhe in Agony",
                        "icon": "spell_shadow_curseofsargeras",
                        "description": "Agony's damage may now ramp up twice as high.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 205181,
                        "name": "Shadowflame",
                        "icon": "ability_warlock_shadowflame",
                        "description": "Lobs a ball of Shadowflame at the target, dealing 6,607 Shadowflame damage immediately, and another 9,248 Shadowflame damage over 8 sec, stacking up to 3 times.\n\n\n\nGenerates 1 Soul Shard.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 205184,
                        "name": "Roaring Blaze",
                        "icon": "ability_warlock_inferno",
                        "description": "Conflagrate increases your remaining Immolate damage on the target by 25% until Immolate expires or is refreshed.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 205145,
                        "name": "Demonic Calling",
                        "icon": "ability_warlock_impoweredimp",
                        "description": "Shadowbolt has a 20% chance, and Demonwrath has a 5% chance on each target, to make your next Call Dreadstalkers cost no Soul Shards.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 198590,
                        "name": "Drain Soul",
                        "icon": "spell_shadow_haunting",
                        "description": "Drains the target's soul, causing 21,990 Shadow damage over 5.5 sec, and healing you for 400% of the damage done.\n\n\n\nGenerates 1 Soul Shard if the target dies during this effect.",
                        "range": "40 yd range",
                        "powerCost": "2% of base mana",
                        "castTime": "Channeled"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 17877,
                        "name": "Shadowburn",
                        "icon": "spell_shadow_scourgebuild",
                        "description": "Blasts a target for 18,920 Shadow damage. \n\n\n\nGenerates 2 Soul Shards if the target dies within 5 sec.",
                        "range": "40 yd range",
                        "powerCost": "0 Soul Shard",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 196105,
                        "name": "Contagion",
                        "icon": "ability_creature_disease_03",
                        "description": "You deal 12% increased damage to targets affected by your Unstable Affliction.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 196270,
                        "name": "Impending Doom",
                        "icon": "spell_shadow_impphaseshift",
                        "description": "Doom also summons 1 Wild Imp when it deals damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 205148,
                        "name": "Reverse Entropy",
                        "icon": "ability_warlock_backdraftgreen",
                        "description": "Reduces the cast time of Chaos Bolt and Rain of Fire by 0.5 sec and they restore 35% of your maximum mana.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 196103,
                        "name": "Absolute Corruption",
                        "icon": "ability_bossmannoroth_empoweredmannorothsgaze",
                        "description": "Corruption is now permanent and deals 25% increased damage. Duration reduced to 40 sec against players.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 196272,
                        "name": "Improved Dreadstalkers",
                        "icon": "ability_warlock_empoweredimp",
                        "description": "Call Dreadstalkers now also summons 2 Wild Imps.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 152108,
                        "name": "Cataclysm",
                        "icon": "achievement_zone_cataclysm",
                        "description": "Conjures a cataclysm at the target location, dealing 46,667 Shadowflame damage to all enemies within 8 yards and afflicting them with Agony, Unstable Affliction, Corruption, or Immolate.",
                        "range": "40 yd range",
                        "castTime": "3 sec cast",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 196104,
                        "name": "Mana Tap",
                        "icon": "spell_shadow_manafeed",
                        "description": "Consumes 25% of your current mana to grant 10% increased damage for 20 sec.",
                        "castTime": "Instant"
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 196277,
                        "name": "Implosion",
                        "icon": "spell_shadow_shadowandflame",
                        "description": "Demonic forces suck all of your Wild Imps toward the target, and then cause them to violently explode, dealing 13,814 Shadowflame damage to all enemies within 8 yards.",
                        "powerCost": "6% of base mana",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 48018,
                        "name": "Demonic Circle",
                        "subtext": "Summon",
                        "icon": "spell_shadow_demoniccirclesummon",
                        "description": "Summons a Demonic Circle for 6 min, allowing you to cast it again to teleport to its location and remove all movement slowing effects. Limit 1.",
                        "powerCost": "5% of base mana",
                        "castTime": "0.5 sec cast"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 6789,
                        "name": "Mortal Coil",
                        "icon": "ability_warlock_mortalcoil",
                        "description": "Horrifies an enemy target into fleeing, incapacitating for 3 sec and healing you for 11% of maximum health.",
                        "range": "20 yd range",
                        "powerCost": "6% of base mana",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 5484,
                        "name": "Howl of Terror",
                        "icon": "ability_warlock_howlofterror",
                        "description": "Let loose a terrifying howl, causing 5 enemies within 10 yds to flee in fear, disorienting them for 20 sec. Damage may cancel the effect.",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 30283,
                        "name": "Shadowfury",
                        "icon": "ability_warlock_shadowfurytga",
                        "description": "Stuns all enemies within 8 yds for 4 sec.",
                        "range": "30 yd range",
                        "castTime": "1.5 sec cast",
                        "cooldown": "30 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 196283,
                        "name": "Hand of Doom",
                        "icon": "ability_warlock_handofguldan",
                        "description": "Hand of Gul'dan now also applies Doom to all enemies it hits.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 196412,
                        "name": "Eradication",
                        "icon": "ability_warlock_eradication",
                        "description": "Chaos Bolt increases the damage you deal to the target by 12% for 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 63106,
                        "name": "Siphon Life",
                        "icon": "spell_shadow_requiem",
                        "description": "Siphons the target's life essence, dealing 17,355 damage over 15 sec and healing you for 100% of the damage it deals.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 196408,
                        "name": "Fire and Brimstone",
                        "icon": "ability_warlock_fireandbrimstone",
                        "description": "Incinerate now hits all enemies near your target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 196226,
                        "name": "Sow the Seeds",
                        "icon": "spell_shadow_seedofdestruction",
                        "description": "Seed of Corruption will now consume a Soul Shard, if available, to embed a demon seed in 4 additional nearby enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Affliction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-affliction",
                        "icon": "spell_shadow_deathcoil",
                        "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 196605,
                        "name": "Power Trip",
                        "icon": "spell_shadow_demonictactics",
                        "description": "Demonic Empowerment has a 50% chance to generate 1 Soul Shard when used in combat.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 196098,
                        "name": "Soul Harvest",
                        "icon": "spell_warlock_demonsoul",
                        "description": "Increases your damage and your pets' damage by 20%.  Lasts 10 sec, increased by 2 sec for each target afflicted by your , up to a maximum of 30 sec.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 219272,
                        "name": "Demon Skin",
                        "icon": "spell_shadow_felarmour",
                        "description": "Your Soul Leech absorption now passively recharges at a rate of 1% of maximum health every 1 sec, and may now absorb up to 20% of maximum health.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 111400,
                        "name": "Burning Rush",
                        "icon": "ability_deathwing_sealarmorbreachtga",
                        "description": "Increases your movement speed by 50%, but also damages you for 4% of your maximum health every 1 sec. Movement impairing effects may not reduce you below 100% of normal movement speed. Lasts until cancelled.",
                        "castTime": "Instant"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 108416,
                        "name": "Dark Pact",
                        "icon": "warlock_sacrificial_pact",
                        "description": "Sacrifices 20% of your demon's current health to shield you for 400% of the sacrificed health for 20 sec. If you have no demon, your health is sacrificed instead. Usable while suffering from control impairing effects.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 152107,
                        "name": "Grimoire of Supremacy",
                        "icon": "warlock_grimoireofcommand",
                        "description": "You are able to maintain control over even greater demons indefinitely, allowing you to summon a Doomguard or Infernal as a permanent pet.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 108501,
                        "name": "Grimoire of Service",
                        "icon": "warlock_grimoireofservice",
                        "description": "Summons a second demon which fights for you for 25 sec and deals 100% increased damage. 1.5 min cooldown. The demon will immmediately use one of its special abilities when summoned:\n\n\n\nGrimoire: Imp: Cleanses 1 harmful Magic effect from you.\n\nGrimoire: Voidwalker Taunts its target.\n\nGrimoire: Succubus Seduces its target.\n\nGrimoire: Felhunter Interrupts its target.\n\nGrimoire: Felguard Stuns its target.",
                        "castTime": "Passive",
                        "cooldown": "1.5 min cooldown"
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 171975,
                        "name": "Grimoire of Synergy",
                        "icon": "warlock_grimoireofsacrifice",
                        "description": "Damage done by you or your demon has a chance to grant the other one 40% increased damage for 15 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 108503,
                        "name": "Grimoire of Sacrifice",
                        "icon": "warlock_grimoireofsacrifice",
                        "description": "Sacrifice your demon to gain Demonic Power, causing your spells to sometimes also deal 6,006 Shadow damage to the target and other enemies within 8 yds. Lasts 1 hour or until you summon a demon.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 205180,
                        "name": "Summon Darkglare",
                        "icon": "achievement_boss_durumu",
                        "description": "Summons a Darkglare for 12 sec that launches Eye Lasers at all targets afflicted by your Doom, dealing 6,607 Shadow damage.",
                        "powerCost": "0 Soul Shard",
                        "castTime": "Instant",
                        "cooldown": "24 sec cooldown"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 196410,
                        "name": "Wreak Havoc",
                        "icon": "ability_warlock_baneofhavoc",
                        "description": "Havoc now lasts 20 sec, and has no cooldown.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 205178,
                        "name": "Soul Effigy",
                        "icon": "trade_archaeology_highbornesoulmirror",
                        "description": "Creates a Soul Effigy bound to the target, which is attackable only by you. 35% of all damage taken by the Effigy is duplicated on the original target. Limit 1. Lasts 10 min.",
                        "range": "40 yd range",
                        "castTime": "1.5 sec cast"
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 157695,
                        "name": "Demonbolt",
                        "icon": "spell_warlock_demonbolt",
                        "description": "Draws energy from your demons and launches a ball of demonic energy at the target, dealing 5,286 Chaos damage. Damage increased 20% for each demon you have active.\n\n\n\nGenerates 1 Soul Shard.",
                        "range": "40 yd range",
                        "powerCost": "4.8% of base mana",
                        "castTime": "2 sec cast"
                    },
                    "spec": {
                        "name": "Demonology",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "spell_shadow_metamorphosis",
                        "description": "A master of demons who compels demonic powers to aid her.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 196447,
                        "name": "Channel Demonfire",
                        "icon": "spell_fire_ragnaros_lavaboltgreen",
                        "description": "Launches 15 bolts of felfire over 2.7 sec at random targets afflicted by your Immolate within 40 yds. Each bolt deals 2,800 Fire damage.",
                        "range": "40 yd range",
                        "powerCost": "4.8% of base mana",
                        "castTime": "Channeled",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Destruction",
                        "role": "DPS",
                        "backgroundImage": "bg-warlock-destruction",
                        "icon": "spell_shadow_rainoffire",
                        "description": "A master of chaos who calls down fire to burn and demolish enemies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 205179,
                        "name": "Phantom Singularity",
                        "icon": "inv_enchant_voidsphere",
                        "description": "Places a phantom singularity above the target, which consumes the life of all enemies within 25 yards, dealing 83,552 damage over 14.6 sec, healing you for 30% of the damage done.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 215941,
                        "name": "Soul Conduit",
                        "icon": "spell_shadow_soulleech_2",
                        "description": "Every Soul Shard you spend has a 20% chance to be refunded.",
                        "castTime": "Passive"
                    }
                }]
            ]
        ],
        "class": "warlock",
        "specs": [{
            "name": "Affliction",
            "role": "DPS",
            "backgroundImage": "bg-warlock-affliction",
            "icon": "spell_shadow_deathcoil",
            "description": "A master of shadow magic who specializes in drains and damage-over-time spells.",
            "order": 0
        }, {
            "name": "Demonology",
            "role": "DPS",
            "backgroundImage": "bg-warlock-demonology",
            "icon": "spell_shadow_metamorphosis",
            "description": "A master of demons who compels demonic powers to aid her.",
            "order": 1
        }, {
            "name": "Destruction",
            "role": "DPS",
            "backgroundImage": "bg-warlock-destruction",
            "icon": "spell_shadow_rainoffire",
            "description": "A master of chaos who calls down fire to burn and demolish enemies.",
            "order": 2
        }]
    },
    "10": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 123986,
                        "name": "Chi Burst",
                        "icon": "spell_arcane_arcanetorrent",
                        "description": "Hurls a torrent of Chi energy up to 40 yds forward, dealing 60,063 Nature damage to all enemies, and 90,094 healing to the Monk and all allies in its path.",
                        "range": "40 yd range",
                        "castTime": "1 sec cast",
                        "cooldown": "30 sec cooldown"
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 124081,
                        "name": "Zen Pulse",
                        "icon": "ability_monk_forcesphere",
                        "description": "Trigger a Zen Pulse around an ally.  Deals 12,012 damage to all enemies within 8 yds of the target. The ally is healed for 12,012 per enemy damaged.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 196607,
                        "name": "Eye of the Tiger",
                        "icon": "ability_druid_primalprecision",
                        "description": "Tiger Palm also applies Eye of the Tiger, dealing 37,568 Nature damage to the enemy and 37,568 healing to the Monk over 8 sec.",
                        "castTime": "Passive"
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 115098,
                        "name": "Chi Wave",
                        "icon": "ability_monk_chiwave",
                        "description": "A wave of Chi energy flows through friends and foes, dealing 18,936 Nature damage or 18,936 healing. Bounces up to 7 times to targets within 25 yards.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 197945,
                        "name": "Mistwalk",
                        "subtext": "Talent",
                        "icon": "spell_lifegivingspeed",
                        "description": "Instantly dash to a friendly player and heal them for 76,444.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 115008,
                        "name": "Chi Torpedo",
                        "icon": "ability_monk_quitornado",
                        "description": "Torpedoes you forward a long distance and increases your movement speed by 30% for 10 sec, stacking up to 2 times.",
                        "castTime": "Instant"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 116841,
                        "name": "Tiger's Lust",
                        "icon": "ability_monk_tigerslust",
                        "description": "Increases a friendly target's movement speed by 70% for 6 sec and removes all roots and snares.",
                        "range": "20 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 115173,
                        "name": "Celerity",
                        "subtext": "Passive Talent",
                        "icon": "ability_monk_quipunch",
                        "description": "Reduces the cooldown of Roll by 5 sec and increases its maximum number of charges by 1.",
                        "castTime": "Passive"
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 196721,
                        "name": "Light Brewing",
                        "icon": "ability_monk_quipunch",
                        "description": "Reduces the cooldown of Ironskin Brew and Purifying Brew by 3 sec and increases their maximum number of charges by 1.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 115288,
                        "name": "Energizing Elixir",
                        "icon": "ability_monk_energizingwine",
                        "description": "Chug an Energizing Elixir, refilling all your Energy and Chi.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 197915,
                        "name": "Lifecycles",
                        "icon": "ability_monk_souldance",
                        "description": "Enveloping Mist reduces the mana cost of your next Vivify by 20%, and Vivify reduces the mana cost of your next Enveloping Mist by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 210802,
                        "name": "Spirit of the Crane",
                        "icon": "monk_stance_redcrane",
                        "description": "Teachings of the Monastery causes each additional Blackout Kick to restore 0.65% mana.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 115399,
                        "name": "Black Ox Brew",
                        "icon": "ability_monk_chibrew",
                        "description": "Chug some Black Ox Brew, which instantly refills your Energy, and your Ironskin Brew and Purifying Brew charges.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 115396,
                        "name": "Ascension",
                        "icon": "ability_monk_ascension",
                        "description": "Increases your maximum Chi by 1, and your Energy regeneration by 10%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 121817,
                        "name": "Power Strikes",
                        "icon": "ability_monk_powerstrikes",
                        "description": "Every 15 sec, your next Tiger Palm generates 1 additional Chi.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 197900,
                        "name": "Mist Wrap",
                        "icon": "ability_monk_pathofmists",
                        "description": "Increases Enveloping Mist's duration by 1 sec and its healing bonus by 10%.\n\n\n\nYou may now channel Soothing Mist while moving.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 196719,
                        "name": "Gift of the Mists",
                        "icon": "ability_monk_pathofmists",
                        "description": "Gift of the Ox has an up to 60% increased chance to trigger, based on your missing health.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 116844,
                        "name": "Ring of Peace",
                        "icon": "spell_monk_ringofpeace",
                        "description": "Form a Ring of Peace around the friendly target for 8 sec. Enemies in the ring that use a harmful spell or ability will be knocked out of the ring.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 196722,
                        "name": "Dizzying Kicks",
                        "icon": "ability_monk_blackoutkick",
                        "description": "Blackout Kick also reduces the target's movement speed by 70% for 3 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 198898,
                        "name": "Song of Chi-Ji",
                        "icon": "inv_chaos_orb",
                        "description": "Conjures a cloud of hypnotic mist that slowly travels forward. Enemies touched by the mist fall asleep, Disoriented for 20 sec.",
                        "range": "40 yd range",
                        "castTime": "1.8 sec cast",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 115315,
                        "name": "Summon Black Ox Statue",
                        "icon": "monk_ability_summonoxstatue",
                        "description": "Summons a Black Ox Statue at the target location for 15 min, pulsing threat to all enemies within 30 yards.\n\n\n\nYou may cast Provoke on the statue to taunt all enemies near the statue.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 119381,
                        "name": "Leg Sweep",
                        "icon": "ability_monk_legsweep",
                        "description": "Knocks down all enemies within 5 yards, stunning them for 5 sec.",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 122281,
                        "name": "Healing Elixir",
                        "icon": "ability_monk_jasmineforcetea",
                        "description": "Drink a healing elixir, healing you for 15% of your maximum health.\n\n\n\nHealing Elixir will automatically trigger if you drop below 35% health, and a charge is available.",
                        "castTime": "Instant"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 122783,
                        "name": "Diffuse Magic",
                        "icon": "spell_monk_diffusemagic",
                        "description": "Reduces magic damage you take by 60% for 6 sec, and transfers all currently active harmful magical effects on you back to their original caster if possible.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 122278,
                        "name": "Dampen Harm",
                        "icon": "ability_monk_dampenharm",
                        "description": "Reduces all damage you take by 30% from the next 3 attacks that damage you for 15% or more of your maximum health. Castable while stunned.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 116847,
                        "name": "Rushing Jade Wind",
                        "icon": "ability_monk_rushingjadewind",
                        "description": "Summons a whirling tornado around you, causing 135,630 damage over 5.5 sec to enemies within 8 yards.",
                        "powerCost": "1 Chi",
                        "castTime": "Instant",
                        "cooldown": "6 sec cooldown"
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 196725,
                        "name": "Refreshing Jade Wind",
                        "icon": "ability_monk_rushingjadewind",
                        "description": "Summon a whirling tornado around you, causing 17,838 healing over 5.5 sec to up to 6 allies within 8 yards, and increasing the healing of Essence Font by 20% while active.",
                        "powerCost": "5% of base mana",
                        "castTime": "Instant",
                        "cooldown": "6 sec cooldown"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 123904,
                        "name": "Invoke Xuen, the White Tiger",
                        "icon": "ability_monk_summontigerstatue",
                        "description": "Summons an effigy of Xuen, the White Tiger for 45 sec. Xuen attacks your primary target, and strikes 3 enemies within 10 yards every 1 sec with Tiger Lightning for 8,737 Nature damage.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 198664,
                        "name": "Invoke Chi-Ji, the Red Crane",
                        "icon": "inv_pet_cranegod",
                        "description": "Summons an effigy of Chi-Ji, the Red Crane for 45 sec. Chi-Ji heals nearby allies with Crane Heal for 29,485.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 132578,
                        "name": "Invoke Niuzao, the Black Ox",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "Summons an effigy of Niuzao, the Black Ox for 45 sec. Niuzao attacks your primary target and taunts it. He also frequently Stomps, damaging all nearby enemies.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 196740,
                        "name": "Hit Combo",
                        "icon": "ability_monk_palmstrike",
                        "description": "Each successive attack that triggers Combo Strikes in a row grants 2% increased damage, stacking up to 8 times.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 196730,
                        "name": "Special Delivery",
                        "icon": "achievement_brewery_2",
                        "description": "Drinking Ironskin or Purifying Brew has a 30% chance to toss a keg high into the air that lands nearby after 3 sec, dealing 176,912 damage to all enemies within 8 yards and reducing their movement speed by 50% for 15 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 115313,
                        "name": "Summon Jade Serpent Statue",
                        "icon": "ability_monk_summonserpentstatue",
                        "description": "Summons a Jade Serpent Statue at the target location. When you channel Soothing Mist, the statue will also channel Soothing Mist on your target, healing for 50% as much.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "10 sec cooldown"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 196743,
                        "name": "Chi Orbit",
                        "icon": "ability_monk_forcesphere",
                        "description": "Every 5 sec, an orb of energy forms, and rotates around you until it impacts an enemy, dealing 32,762 damage to all nearby enemies. Maximum 4 orbs.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 197908,
                        "name": "Mana Tea",
                        "icon": "monk_ability_cherrymanatea",
                        "description": "Reduces the mana cost of your spells by 50% for 10 sec.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 196738,
                        "name": "Elusive Dance",
                        "icon": "ability_monk_shuffle",
                        "description": "Purifying Brew now clears an additional 15% of damage delayed with Stagger.\n\n\n\nIt also grants up to 15% Dodge and damage done for 6 sec, based on the level of Stagger damage purified.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 197895,
                        "name": "Focused Thunder",
                        "icon": "spell_monk_nimblebrew",
                        "description": "Thunder Focus Tea now empowers your next 2 spells.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 152175,
                        "name": "Whirling Dragon Punch",
                        "icon": "ability_monk_hurricanestrike",
                        "description": "Performs a devastating whirling upward strike, dealing 271,920 damage to all nearby enemies. Only usable while Fists of Fury and Rising Sun Kick are on cooldown.",
                        "castTime": "Instant",
                        "cooldown": "24 sec cooldown"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 196736,
                        "name": "Blackout Combo",
                        "icon": "ability_monk_blackoutkick",
                        "description": "Blackout Strike also empowers your next ability:\n\n\n\nTiger Palm: Damage increased by 200%.\n\nBreath of Fire: Cooldown reduced by 6 sec.\n\nKeg Smash: Reduces the remaining cooldown on your Brews by 2 additional sec.\n\nIronskin Brew: Pauses Stagger damage for 3 sec.\n\nPurifying Brew: Grants you a stack of Elusive Brawler.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 196737,
                        "name": "High Tolerance",
                        "icon": "monk_ability_avertharm",
                        "description": "Stagger delays an additional 10% of incoming damage.\n\n\n\nYou gain up to 15% Haste based on your current level of Stagger.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Brewmaster",
                        "role": "TANK",
                        "backgroundImage": "bg-monk-brewmaster",
                        "icon": "spell_monk_brewmaster_spec",
                        "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 210804,
                        "name": "Rising Thunder",
                        "icon": "ability_thunderking_lightningwhip",
                        "description": "Rising Sun Kick resets the remaining cooldown on Thunder Focus Tea.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Mistweaver",
                        "role": "HEALING",
                        "backgroundImage": "bg-monk-mistweaver",
                        "icon": "spell_monk_mistweaver_spec",
                        "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 152173,
                        "name": "Serenity",
                        "icon": "ability_monk_serenity",
                        "description": "Enter an elevated state of mental and physical serenity for 8 sec. While in this state, you deal 40% increased damage and healing, and all Chi consumers are free and have 50% reduced cooldown.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Windwalker",
                        "role": "DPS",
                        "backgroundImage": "bg-monk-battledancer",
                        "icon": "spell_monk_windwalker_spec",
                        "description": "A martial artist without peer who pummels foes with hands and fists.",
                        "order": 2
                    }
                }]
            ]
        ],
        "class": "monk",
        "specs": [{
            "name": "Brewmaster",
            "role": "TANK",
            "backgroundImage": "bg-monk-brewmaster",
            "icon": "spell_monk_brewmaster_spec",
            "description": "A sturdy brawler who uses liquid fortification and unpredictable movement to avoid damage and protect allies.",
            "order": 0
        }, {
            "name": "Mistweaver",
            "role": "HEALING",
            "backgroundImage": "bg-monk-mistweaver",
            "icon": "spell_monk_mistweaver_spec",
            "description": "A healer who masters the mysterious art of manipulating life energies, aided by the wisdom of the Jade Serpent and Pandaren medicinal techniques.",
            "order": 1
        }, {
            "name": "Windwalker",
            "role": "DPS",
            "backgroundImage": "bg-monk-battledancer",
            "icon": "spell_monk_windwalker_spec",
            "description": "A martial artist without peer who pummels foes with hands and fists.",
            "order": 2
        }]
    },
    "11": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 205636,
                        "name": "Force of Nature",
                        "subtext": "Talent",
                        "icon": "ability_druid_forceofnature",
                        "description": "Summons a stand of 3 Treants for 10 sec which immediately taunt and attack enemies in the targeted area.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 200383,
                        "name": "Prosperity",
                        "subtext": "Passive Talent",
                        "icon": "spell_druid_rampantgrowth",
                        "description": "Swiftmend now has 2 charges, and its cooldown is reduced by 3 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 203953,
                        "name": "Brambles",
                        "icon": "inv_misc_thornnecklace",
                        "description": "Sharp brambles protect you, absorbing and reflecting up to 5,241 damage from each attack.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 202021,
                        "name": "Predator",
                        "icon": "ability_hunter_catlikereflexes",
                        "description": "The cooldown on Tiger's Fury resets when a target dies with one of your Bleed effects active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 202022,
                        "name": "Blood Scent",
                        "icon": "ability_mount_pinktiger",
                        "description": "Your melee abilities in Cat Form have a 10% increased critical strike chance on targets with a Bleed effect.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 155835,
                        "name": "Bristling Fur",
                        "icon": "spell_druid_bristlingfur",
                        "description": "Bristle your fur, causing you to generate Rage based on damage taken for 8 sec.",
                        "castTime": "Instant",
                        "cooldown": "40 sec cooldown"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 102351,
                        "name": "Cenarion Ward",
                        "icon": "ability_druid_naturalperfection",
                        "description": "Protects a friendly target for 30 sec. Any damage taken will consume the ward and heal the target for 52,852 over 8 sec.",
                        "range": "40 yd range",
                        "powerCost": "9.19% of base mana",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 202425,
                        "name": "Warrior of Elune",
                        "icon": "spell_holy_elunesgrace",
                        "description": "Your next 2 Lunar Strikes are instant cast.",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 202345,
                        "name": "Starlord",
                        "icon": "spell_shaman_measuredinsight",
                        "description": "Lunar and Solar Empowerments also reduce the cast time of their affected spells by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 207383,
                        "name": "Abundance",
                        "icon": "ability_druid_empoweredrejuvination",
                        "description": "For each Rejuvenation you have active, the cast time of Healing Touch is reduced by 10%, and the critical effect chance of Regrowth is increased by 10%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 203962,
                        "name": "Blood Frenzy",
                        "icon": "ability_druid_primaltenacity",
                        "description": "Thrash also generates 2 Rage each time it deals damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 155580,
                        "name": "Lunar Inspiration",
                        "icon": "spell_druid_lunarinspiration",
                        "description": "Moonfire is now usable while in Cat Form, generates 1 combo point, deals damage based on attack power, and costs 30 energy.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 204012,
                        "name": "Guttural Roars",
                        "icon": "ability_druid_enrage",
                        "description": "Increases the radius of Stampeding Roar by 200%, the radius of Incapacitating Roar by 100%, and reduces the cooldown of Stampeding Roar by 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 108238,
                        "name": "Renewal",
                        "icon": "spell_nature_natureblessing",
                        "description": "Instantly heals you for 30% of maximum health. Usable in all shapeshift forms.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 102280,
                        "name": "Displacer Beast",
                        "icon": "spell_druid_displacement",
                        "description": "Teleports you up to 20 yards forward, activating Cat Form and increasing your movement speed by 50% for 4 sec.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 102401,
                        "name": "Wild Charge",
                        "icon": "spell_druid_wildcharge",
                        "description": "Fly to a nearby ally's position.",
                        "range": "5-25 yd range",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 197632,
                        "name": "Balance Affinity",
                        "icon": "ability_druid_improvedmoonkinform",
                        "description": "You gain:\n\n\n\n Astral Influence\n\nIncreases the range of all of your abilities by 5 yards.\n\n\n\nYou also learn:\n\n\n\n Moonkin Form\n\n Starsurge\n\n Lunar Strike",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 197488,
                        "name": "Balance Affinity",
                        "icon": "ability_druid_improvedmoonkinform",
                        "description": "You gain:\n\n\n\n Astral Influence\n\nIncreases the range of all of your abilities by 5 yards.\n\n\n\nYou also learn:\n\n\n\n Moonkin Form\n\n Starsurge\n\n Lunar Strike\n\n Solar Wrath\n\n Sunfire",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 202157,
                        "name": "Feral Affinity",
                        "icon": "talentspec_druid_feral_cat",
                        "description": "You gain:\n\n\n\n Feline Swiftness\n\nIncreases your movement speed by 15%.\n\n\n\nYou also learn:\n\n\n\n Shred\n\n Rake\n\n Rip\n\n Ferocious Bite\n\n Swipe\n\n\n\nYour energy regeneration is increased by 35%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 197490,
                        "name": "Feral Affinity",
                        "icon": "talentspec_druid_feral_cat",
                        "description": "You gain:\n\n\n\n Feline Swiftness\n\nIncreases your movement speed by 15%.\n\n\n\nYou also learn:\n\n\n\n Shred\n\n Rake\n\n Rip\n\n Ferocious Bite\n\n Swipe\n\n\n\nYour energy regeneration is increased by 35%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 197491,
                        "name": "Guardian Affinity",
                        "icon": "talentspec_druid_feral_bear",
                        "description": "You gain:\n\n\n\n Thick Hide\n\nReduces all damage taken by 10%.\n\n\n\nYou also learn:\n\n\n\n Mangle\n\n Thrash\n\n Ironfur\n\n Frenzied Regeneration",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 217615,
                        "name": "Guardian Affinity",
                        "icon": "talentspec_druid_feral_bear",
                        "description": "You gain:\n\n\n\n Thick Hide\n\nReduces all damage taken by 10%.\n\n\n\nYou also learn:\n\n\n\n Mangle\n\n Ironfur\n\n Frenzied Regeneration",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 202155,
                        "name": "Feral Affinity",
                        "icon": "talentspec_druid_feral_cat",
                        "description": "You gain:\n\n\n\n Feline Swiftness\n\nIncreases your movement speed by 15%.\n\n\n\nYou also learn:\n\n\n\n Shred\n\n Rake\n\n Rip\n\n Ferocious Bite\n\n\n\nYour energy regeneration is increased by 35%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 197492,
                        "name": "Restoration Affinity",
                        "icon": "ability_druid_improvedtreeform",
                        "description": "You gain:\n\n\n\n Ysera's Gift\n\nHeals you for 3% of your maximum health every 5 sec. If you are at full health, a injured party or raid member will be healed instead.\n\n\n\nYou also learn:\n\n\n\n Rejuvenation\n\n Healing Touch\n\n Swiftmend",
                        "castTime": "Passive"
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 197491,
                        "name": "Guardian Affinity",
                        "icon": "talentspec_druid_feral_bear",
                        "description": "You gain:\n\n\n\n Thick Hide\n\nReduces all damage taken by 10%.\n\n\n\nYou also learn:\n\n\n\n Mangle\n\n Thrash\n\n Ironfur\n\n Frenzied Regeneration",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 5211,
                        "name": "Mighty Bash",
                        "icon": "ability_druid_bash",
                        "description": "Invokes the spirit of Ursoc to stun the target for 5 sec. Usable in all shapeshift forms.",
                        "range": "Melee Range",
                        "castTime": "Instant",
                        "cooldown": "50 sec cooldown"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 102359,
                        "name": "Mass Entanglement",
                        "icon": "spell_druid_massentanglement",
                        "description": "Roots the target in place for 20 sec and spreads to additional nearby enemies. Damage may interrupt the effect. Usable in all shapeshift forms.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 132469,
                        "name": "Typhoon",
                        "icon": "ability_druid_typhoon",
                        "description": "Strikes targets within 15 yards in front of you with a violent Typhoon, knocking them back and dazing them for 6 sec. Usable in all shapeshift forms.",
                        "castTime": "Instant",
                        "cooldown": "30 sec cooldown"
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 114107,
                        "name": "Soul of the Forest",
                        "icon": "ability_druid_manatree",
                        "description": "Increases the damage bonus from Lunar and Solar Empowerment by an additional 15%.\n\n\n\nReduces the Astral Power cost of Starfall by 10.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 158476,
                        "name": "Soul of the Forest",
                        "icon": "ability_druid_manatree",
                        "description": "Your finishing moves grant 12 Energy per combo point.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 158478,
                        "name": "Soul of the Forest",
                        "icon": "ability_druid_manatree",
                        "description": "When you cast Swiftmend, you gain Soul of the Forest,  increasing the healing of your next Regrowth or Rejuvenation by 200%, or increasing the healing of your next Wild Growth by 75%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 158477,
                        "name": "Soul of the Forest",
                        "icon": "ability_druid_manatree",
                        "description": "Mangle generates 5 more Rage and deals 15% more damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 33891,
                        "name": "Incarnation: Tree of Life",
                        "subtext": "Talent, Shapeshift",
                        "icon": "ability_druid_improvedtreeform",
                        "description": "Shapeshift into the Tree of Life, increasing healing done by 15%, increasing armor by 120%, and granting protection from Polymorph effects.  Functionality of Rejuvenation, Wild Growth, Regrowth, and Entangling Roots is enhanced.\n\n\n\nLasts 30 sec. You may shapeshift in and out of this form for its duration.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 102560,
                        "name": "Incarnation: Chosen of Elune",
                        "subtext": "Talent, Shapeshift",
                        "icon": "spell_druid_incarnation",
                        "description": "An improved Moonkin Form that increases the damage of all your spells by 35% and causes your Lunar Strike and Solar Wrath to generate 50% additional Astral Power.\n\n\n\nLasts 30 sec. You may shapeshift in and out of this improved Moonkin Form for its duration.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 102558,
                        "name": "Incarnation: Guardian of Ursoc",
                        "subtext": "Talent, Shapeshift",
                        "icon": "spell_druid_incarnation",
                        "description": "An improved Bear Form that reduces the cooldown on all melee damage abilities and Growl to 1.5 sec, and causes Mangle to hit up to 3 targets.\n\n\n\nLasts 30 sec. You may freely shapeshift in and out of this improved Bear Form for its duration.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 102543,
                        "name": "Incarnation: King of the Jungle",
                        "subtext": "Talent, Shapeshift",
                        "icon": "spell_druid_incarnation",
                        "description": "An improved Cat Form that allows the use of Prowl while in combat, causes Shred and Rake to deal damage as if stealth were active, reduces the cost of all Cat Form abilities by 50%, and increases maximum Energy by 50.\n\n\n\nLasts 30 sec. You may shapeshift in and out of this improved Cat Form for its duration.",
                        "castTime": "Instant",
                        "cooldown": "3 min cooldown"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 200390,
                        "name": "Cultivation",
                        "icon": "ability_druid_nourish",
                        "description": "When Rejuvenation heals a target below 60% health, it applies Cultivation to the target, healing them for 8,648 over 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 52610,
                        "name": "Savage Roar",
                        "icon": "ability_druid_skinteeth",
                        "description": "Finishing move that grants 25% increased damage to your Cat Form attacks for their full duration. Lasts longer per combo point:\n\n\n\n   1 point  : 8 seconds\n\n   2 points: 12 seconds\n\n   3 points: 16 seconds\n\n   4 points: 20 seconds\n\n   5 points: 24 seconds",
                        "powerCost": "40 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 203964,
                        "name": "Galactic Guardian",
                        "icon": "spell_frost_iceclaw",
                        "description": "Your damage has a 10% chance to trigger a free automatic Moonfire on that target. \n\n\n\nWhen this occurs, the next Moonfire you cast generates 10 Rage, and deals 300% increased direct damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 202347,
                        "name": "Stellar Flare",
                        "icon": "ability_druid_stellarflare",
                        "description": "Burns the target for 12,013 Astral  damage, and then an additional 46,860 damage over 24 sec.\n\n\n\nStellar Flare benefits from Starfall's Stellar Empowerment.",
                        "range": "40 yd range",
                        "powerCost": "",
                        "castTime": "1.5 sec cast"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 207385,
                        "name": "Spring Blossoms",
                        "icon": "inv_misc_trailofflowers",
                        "description": "Each target healed by Efflorescence is healed for an additional 3,603 over 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 202031,
                        "name": "Sabertooth",
                        "icon": "inv_misc_monsterfang_01",
                        "description": "Ferocious Bite always refreshes the duration of Rip.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 202342,
                        "name": "Shooting Stars",
                        "icon": "spell_priest_divinestar_shadow2",
                        "description": "Moonfire and Sunfire damage over time has a 10% chance to call down a falling star, dealing 2,333 Astral damage and generating 4 Astral Power.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 203974,
                        "name": "Earthwarden",
                        "icon": "spell_shaman_blessingofeternals",
                        "description": "Every 6 sec, you gain a charge of Earthwarden, reducing the damage of the next auto attack you take by 30%. Earthwarden may have up to 3 charges.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 197073,
                        "name": "Inner Peace",
                        "icon": "ability_druid_dreamstate",
                        "description": "Reduces the cooldown of Tranquility by 60 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 202032,
                        "name": "Jagged Wounds",
                        "icon": "ability_druid_disembowel",
                        "description": "Your Rip, Rake, and Thrash abilities deal the same damage as normal, but in 33% less time.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 155578,
                        "name": "Guardian of Elune",
                        "icon": "spell_druid_guardianofelune",
                        "description": "Mangle increases the duration of your next Ironfur or Mark of Ursol by 2 sec, or the healing of your next Frenzied Regeneration by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 202359,
                        "name": "Astral Communion",
                        "icon": "talentspec_druid_balance",
                        "description": "Generates 75 Astral Power.",
                        "castTime": "Instant",
                        "cooldown": "1.33 min cooldown"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 202060,
                        "name": "Elune's Guidance",
                        "icon": "spell_holy_elunesgrace",
                        "description": "Immediately gain 5 combo points and an additional 1 combo point every 1 sec for 5 sec.",
                        "castTime": "Instant",
                        "cooldown": "45 sec cooldown"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 203965,
                        "name": "Survival of the Fittest",
                        "icon": "ability_druid_enrage",
                        "description": "Reduces the cooldowns of Barkskin and Survival Instincts by 33%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 202360,
                        "name": "Blessing of the Ancients",
                        "icon": "inv_pet_ancientprotector",
                        "description": "Gain a Blessing of the Ancients, activating or swapping between one of the two following beneficial effects:\n\n\n\n Blessing of Elune\n\nIncreases Astral Power generated by Solar Wrath and Lunar Strike by 25%.\n\n\n\n Blessing of An'she\n\nGrants 2 Astral Power every 3 sec.",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 155675,
                        "name": "Germination",
                        "icon": "spell_druid_germination",
                        "description": "You can apply Rejuvenation twice to the same target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 204053,
                        "name": "Rend and Tear",
                        "icon": "ability_druid_swipe",
                        "description": "While in Bear Form, Thrash also increases your damage dealt to the target, and reduces your damage taken from the target by 2% per application of Thrash.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 202770,
                        "name": "Fury of Elune",
                        "icon": "ability_druid_dreamstate",
                        "description": "Calls down a beam of pure celestial energy at the target location, dealing 17,418 Astral damage every 1 sec until your Astral Power is exhausted.\n\n\n\nWhile Fury of Elune is active, you may recast it for no cost to direct the beam to move to a new location.",
                        "range": "40 yd range",
                        "powerCost": "",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 155577,
                        "name": "Moment of Clarity",
                        "icon": "spell_druid_momentofclarity",
                        "description": "Omen of Clarity now affects the next 3 Regrowths.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 202028,
                        "name": "Brutal Slash",
                        "icon": "ability_druid_ravage",
                        "description": "Strikes all nearby enemies with a massive slash, inflicting 520,634 Physical damage. Awards 1 combo point. Maximum 3 charges.",
                        "range": "8 yd range",
                        "powerCost": "20 Energy",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 155672,
                        "name": "Bloodtalons",
                        "icon": "spell_druid_bloodythrash",
                        "description": "Casting Regrowth causes your next two melee abilities to deal 50% increased damage for their full duration.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 204066,
                        "name": "Lunar Beam",
                        "icon": "spell_nature_moonglow",
                        "description": "Summons a beam of lunar light at your location, dealing 157,256 Arcane damage and healing you for 524,184 over 8 sec.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 202354,
                        "name": "Stellar Drift",
                        "icon": "spell_nature_starfall",
                        "description": "Increases Starfall's radius by 30%, Starfall damage by 20%, and allows you to cast while moving while within Starfall's radius.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 197061,
                        "name": "Stonebark",
                        "icon": "ability_druid_replenish",
                        "description": "Reduces the cooldown of Ironbark by 30 sec, and it increases healing from your heal over time effects by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 155577,
                        "name": "Moment of Clarity",
                        "icon": "spell_druid_momentofclarity",
                        "description": "Omen of Clarity now affects the next 3 Regrowths.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Feral",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-cat",
                        "icon": "ability_druid_catform",
                        "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 80313,
                        "name": "Pulverize",
                        "icon": "spell_druid_malfurionstenacity",
                        "description": "A devastating blow that consumes 2 stacks of your Thrash on the target to deal 145,777 Physical damage, and reduces all damage you take by 8% for 20 sec.",
                        "range": "Melee Range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Guardian",
                        "role": "TANK",
                        "backgroundImage": "bg-druid-bear",
                        "icon": "ability_racial_bearform",
                        "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
                        "order": 2
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 202430,
                        "name": "Nature's Balance",
                        "icon": "ability_druid_balanceofpower",
                        "description": "Aligns the power of the Moon and Stars, causing Lunar Strike to extend the duration of your Moonfire by 6.0 sec, and Solar Wrath to extend the duration of all of your Sunfires by 4.0 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Balance",
                        "role": "DPS",
                        "backgroundImage": "bg-druid-balance",
                        "icon": "spell_nature_starfall",
                        "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 197721,
                        "name": "Flourish",
                        "icon": "spell_druid_wildburst",
                        "description": "Extends the duration of all of your heal over time effects on friendly targets within 60 yards by 6 sec.",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Restoration",
                        "role": "HEALING",
                        "backgroundImage": "bg-druid-restoration",
                        "icon": "spell_nature_healingtouch",
                        "description": "Uses heal-over-time Nature spells to keep allies alive.",
                        "order": 3
                    }
                }]
            ]
        ],
        "class": "druid",
        "specs": [{
            "name": "Balance",
            "role": "DPS",
            "backgroundImage": "bg-druid-balance",
            "icon": "spell_nature_starfall",
            "description": "Can take on the form of a powerful Moonkin, balancing the power of Arcane and Nature magic to destroy enemies at a distance.",
            "order": 0
        }, {
            "name": "Feral",
            "role": "DPS",
            "backgroundImage": "bg-druid-cat",
            "icon": "ability_druid_catform",
            "description": "Takes on the form of a great cat to deal damage with bleeds and bites.",
            "order": 1
        }, {
            "name": "Guardian",
            "role": "TANK",
            "backgroundImage": "bg-druid-bear",
            "icon": "ability_racial_bearform",
            "description": "Takes on the form of a mighty bear to absorb damage and protect allies.",
            "order": 2
        }, {
            "name": "Restoration",
            "role": "HEALING",
            "backgroundImage": "bg-druid-restoration",
            "icon": "spell_nature_healingtouch",
            "description": "Uses heal-over-time Nature spells to keep allies alive.",
            "order": 3
        }]
    },
    "12": {
        "talents": [
            [
                [{
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 192939,
                        "name": "Fel Mastery",
                        "icon": "ability_skyreach_piercing_rush",
                        "description": "Increases Fel Rush damage by 30%, and grants 25 Fury when Fel Rush damages at least one target.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 0,
                    "spell": {
                        "id": 207550,
                        "name": "Abyssal Strike",
                        "icon": "spell_warlock_summonabyssal",
                        "description": "Infernal Strike's range is increased by 10 yards, and its cooldown is reduced by 5 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 207548,
                        "name": "Agonizing Flames",
                        "icon": "achievment_raid_houroftwilight",
                        "description": "Immolation Aura increases your movement speed by 30%, and deals 30% increased damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 0,
                    "column": 1,
                    "spell": {
                        "id": 206475,
                        "name": "Chaos Cleave",
                        "icon": "inv_weapon_shortblade_62",
                        "description": "Chaos Strike hits an additional target for 50% damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 203550,
                        "name": "Blind Fury",
                        "icon": "ability_bosskilrogg_deadeye",
                        "description": "Increases the duration of Eye Beam by 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 0,
                    "column": 2,
                    "spell": {
                        "id": 209400,
                        "name": "Razor Spikes",
                        "icon": "ability_demonhunter_demonspikes2",
                        "description": "While Demon Spikes is active, you deal 20% increased Physical damage and your melee attacks snare targets by 50% for 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 207697,
                        "name": "Feast of Souls",
                        "icon": "spell_shadow_soulleech",
                        "description": "Soul Cleave heals you for an additional 85,179 over 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 0,
                    "spell": {
                        "id": 203551,
                        "name": "Prepared",
                        "icon": "ability_demonhunter_vengefulretreat",
                        "description": "Reduces the cooldown of Vengeful Retreat by 10 sec, and generates 40 Fury over 5 sec if you damage at least one enemy with Vengeful Retreat.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 227174,
                        "name": "Fallout",
                        "icon": "spell_volatilefiregreen",
                        "description": "Immolation Aura's initial burst has a chance to shatter Lesser Soul Fragments from enemies.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 1,
                    "column": 1,
                    "spell": {
                        "id": 203555,
                        "name": "Demon Blades",
                        "icon": "inv_weapon_shortblade_92",
                        "description": "Your auto attacks have a 75% chance to deal additional Shadow damage and generate Fury.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 206478,
                        "name": "Demonic Appetite",
                        "icon": "spell_misc_zandalari_council_soulswap",
                        "description": "Chaos Strike has a chance to spawn a Lesser Soul Fragment, and consuming any Soul Fragment grants 30 Fury.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 1,
                    "column": 2,
                    "spell": {
                        "id": 207739,
                        "name": "Burning Alive",
                        "icon": "spell_fire_elementaldevastation",
                        "description": "Every 2 sec, your Fiery Brand deals 9,828 Fire damage and spreads from the primary target to a nearby enemy.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 2,
                    "column": 0,
                    "spell": {
                        "id": 232893,
                        "name": "Felblade",
                        "icon": "ability_demonhunter_felblade",
                        "description": "Charge to your target and deal 144,011 Fire damage.\n\n\n\nDemon's Bite has a chance to reset the cooldown of Felblade.\n\n\n\nGenerates 30 Fury.",
                        "range": "15 yd range",
                        "castTime": "Instant",
                        "cooldown": "15 sec cooldown"
                    }
                }],
                [{
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 227322,
                        "name": "Flame Crash",
                        "icon": "spell_fire_felhellfire",
                        "description": "Infernal Strike creates a Sigil of Flame when you land.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 2,
                    "column": 1,
                    "spell": {
                        "id": 206416,
                        "name": "First Blood",
                        "icon": "ability_deathwing_bloodcorruption_death",
                        "description": "Reduces the Fury cost of Blade Dance by 20 and increases its damage to 247,019 against the first target struck.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 206473,
                        "name": "Bloodlet",
                        "icon": "ability_demonhunter_bloodlet",
                        "description": "Throw Glaive causes targets to bleed for 150% of the damage inflicted over 10 sec. If this effect is reapplied, any remaining damage will be added to the new Bloodlet.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 2,
                    "column": 2,
                    "spell": {
                        "id": 211881,
                        "name": "Fel Eruption",
                        "icon": "ability_bossfellord_felspike",
                        "description": "Impales the target for 229,331 Chaos damage and stuns them for 2 sec.  Inflicts an additional 100% damage against targets permanently immune to stuns.",
                        "range": "20 yd range",
                        "powerCost": "10 Pain",
                        "castTime": "Instant",
                        "cooldown": "35 sec cooldown"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 196555,
                        "name": "Netherwalk",
                        "icon": "spell_warlock_demonsoul",
                        "description": "Slip into the nether, increasing movement speed by 100% and becoming immune to damage, but unable to attack. Lasts 5 sec.",
                        "castTime": "Instant",
                        "cooldown": "1.5 min cooldown"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 0,
                    "spell": {
                        "id": 218612,
                        "name": "Feed the Demon",
                        "icon": "spell_warlock_demonicempowerment",
                        "description": "Consuming a Soul Fragment reduces the remaining cooldown of Demon Spikes by 1 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 205411,
                        "name": "Desperate Instincts",
                        "icon": "spell_shadow_manafeed",
                        "description": "You automatically trigger Blur when you fall below 35% health.  This effect can occur every 30 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 3,
                    "column": 1,
                    "spell": {
                        "id": 209795,
                        "name": "Fracture",
                        "icon": "ability_creature_felsunder",
                        "description": "Brutally slam your target for 144,363 Physical damage, and shatter two Lesser Soul Fragments from them.",
                        "range": "Melee Range",
                        "powerCost": "40 Pain",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 217996,
                        "name": "Soul Rending",
                        "icon": "ability_demonhunter_soulcleave2",
                        "description": "Gain 50% Leech while Metamorphosis is active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 3,
                    "column": 2,
                    "spell": {
                        "id": 204909,
                        "name": "Soul Rending",
                        "icon": "ability_demonhunter_soulcleave2",
                        "description": "Gain 100% Leech while Metamorphosis is active.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 207666,
                        "name": "Concentrated Sigils",
                        "icon": "ability_bossfelorcs_necromancer_red",
                        "description": "All Sigils are now targeted at your location, and the duration of their effects is increased by 2 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 0,
                    "spell": {
                        "id": 206476,
                        "name": "Momentum",
                        "icon": "ability_foundryraid_demolition",
                        "description": "Fel Rush and Vengeful Retreat increase your damage done by 20% for 4 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 211881,
                        "name": "Fel Eruption",
                        "icon": "ability_bossfellord_felspike",
                        "description": "Impales the target for 229,331 Chaos damage and stuns them for 2 sec.  Inflicts an additional 100% damage against targets permanently immune to stuns.",
                        "range": "20 yd range",
                        "powerCost": "10 Pain",
                        "castTime": "Instant",
                        "cooldown": "35 sec cooldown"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 4,
                    "column": 1,
                    "spell": {
                        "id": 202138,
                        "name": "Sigil of Chains",
                        "icon": "ability_demonhunter_sigilofchains",
                        "description": "Place a Sigil of Chains at the target location that activates after 2 sec.\n\n\n\nAll enemies affected by the sigil are pulled to its center and are snared, reducing movement speed by 70% for 6 sec.",
                        "range": "30 yd range",
                        "castTime": "Instant",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 209281,
                        "name": "Quickened Sigils",
                        "icon": "ability_demonhunter_concentratedsigils",
                        "description": "All Sigils activate 1 second faster, and their cooldowns are reduced by 20%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 4,
                    "column": 2,
                    "spell": {
                        "id": 206491,
                        "name": "Nemesis",
                        "icon": "ability_warlock_improveddemonictactics",
                        "description": "Increases damage you inflict against the target by 20% for 1 min. \n\n\n\nWhen the target is slain, you will inflict 20% additional damage against all creature types matching the original target (Humanoid, Dragonkin, etc.) for the remaining duration.",
                        "range": "50 yd range",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }]
            ],
            [
                [{
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 212084,
                        "name": "Fel Devastation",
                        "icon": "ability_demonhunter_feldevastation",
                        "description": "Unleash the fel within you, damaging enemies directly in front of you for 196,580 Fire damage over 1.8 sec. Causing damage also heals you for up to 546,030 health.",
                        "range": "20 yd range",
                        "powerCost": "30 Pain",
                        "castTime": "Channeled",
                        "cooldown": "1 min cooldown"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 5,
                    "column": 0,
                    "spell": {
                        "id": 203556,
                        "name": "Master of the Glaive",
                        "icon": "inv_glaive_1h_demonhunter_a_01",
                        "description": "Throw Glaive now has 2 charges, and snares all enemies hit by 50% for 6 sec.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 206477,
                        "name": "Unleashed Power",
                        "icon": "ability_demonhunter_chaosnova",
                        "description": "Removes the Fury cost of Chaos Nova and reduces its cooldown by 33%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 1,
                    "spell": {
                        "id": 203753,
                        "name": "Blade Turning",
                        "icon": "trade_archaeology_zinrokhsword",
                        "description": "Parrying an attack increases the Pain generation of your next Shear by 50%.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 193897,
                        "name": "Demon Reborn",
                        "icon": "ability_warlock_demonicempowerment",
                        "description": "Invoking Metamorphosis also resets the cooldowns of Eye Beam, Chaos Nova, and Blur.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 5,
                    "column": 2,
                    "spell": {
                        "id": 218679,
                        "name": "Spirit Bomb",
                        "icon": "inv_icon_shadowcouncilorb_purple",
                        "description": "Launch a nearby Soul Fragment at your target, dealing 55,039 Shadow damage to all nearby enemies and afflicting them with Frailty for 15 sec.\n\n\n\nYou heal for 15% of all damage you deal to enemies with Frailty.",
                        "range": "40 yd range",
                        "castTime": "Instant"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }]
            ],
            [
                [{
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 209258,
                        "name": "Last Resort",
                        "icon": "inv_glaive_1h_artifactaldorchi_d_06",
                        "description": "Sustaining fatal damage instead transforms you to Metamorphosis form, and returns you to 30% health.\n\n\n\nThis effect may only occur every 3 min.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }, {
                    "tier": 6,
                    "column": 0,
                    "spell": {
                        "id": 211048,
                        "name": "Chaos Blades",
                        "icon": "inv_glaive_1h_artifactaldrochi_d_03dual",
                        "description": "Increases all damage done by 44% (based on Mastery) for 12 sec.\n\n\n\nWhile active, your auto attack deals 200% increased damage, and causes Chaos damage.",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }],
                [{
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 211053,
                        "name": "Fel Barrage",
                        "icon": "ability_felarakkoa_feldetonation_green",
                        "description": "At your command, unleash Fel, inflicting 54,603 Chaos damage to your target and nearby enemies for each charge.  Max 5 charges.\n\n\n\nYour damaging abilities have a chance to generate a charge.",
                        "range": "30 yd range",
                        "castTime": "Channeled"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 1,
                    "spell": {
                        "id": 207810,
                        "name": "Nether Bond",
                        "icon": "ability_demonhunter_netherbond",
                        "description": "Bind yourself to a friendly player for 15 sec. Every 1 sec, the health of you and your target is redistributed such that you are at the same percentage of maximum health.",
                        "range": "40 yd range",
                        "castTime": "Instant",
                        "cooldown": "2 min cooldown"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }],
                [{
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 213410,
                        "name": "Demonic",
                        "icon": "spell_shadow_demonform",
                        "description": "Eye Beam causes you to enter demon form for 5 sec after it finishes dealing damage.",
                        "castTime": "Passive"
                    },
                    "spec": {
                        "name": "Havoc",
                        "role": "DPS",
                        "backgroundImage": "bg-rogue-subtlety",
                        "icon": "ability_demonhunter_specdps",
                        "description": "A brooding master of warglaives and the destructive power of Fel magic.",
                        "order": 0
                    }
                }, {
                    "tier": 6,
                    "column": 2,
                    "spell": {
                        "id": 227225,
                        "name": "Soul Barrier",
                        "icon": "inv_glaive_1h_artifactaldrochi_d_05",
                        "description": "Shield yourself for 12 sec, absorbing 327,615 damage. Consuming a Soul Fragment adds 54,602 to the shield.\n\n\n\nSoul Barrier's absorption cannot be reduced below 43,682.\n\n\n\nConsumes all Soul Fragments within 25 yds.",
                        "powerCost": "30 Pain",
                        "castTime": "Instant",
                        "cooldown": "20 sec cooldown"
                    },
                    "spec": {
                        "name": "Vengeance",
                        "role": "TANK",
                        "backgroundImage": "bg-warlock-demonology",
                        "icon": "ability_demonhunter_spectank",
                        "description": "Embraces the demon within to incinerate enemies and protect their allies.",
                        "order": 1
                    }
                }]
            ]
        ],
        "class": "demon-hunter",
        "specs": [{
            "name": "Havoc",
            "role": "DPS",
            "backgroundImage": "bg-rogue-subtlety",
            "icon": "ability_demonhunter_specdps",
            "description": "A brooding master of warglaives and the destructive power of Fel magic.",
            "order": 0
        }, {
            "name": "Vengeance",
            "role": "TANK",
            "backgroundImage": "bg-warlock-demonology",
            "icon": "ability_demonhunter_spectank",
            "description": "Embraces the demon within to incinerate enemies and protect their allies.",
            "order": 1
        }]
    }
}

# https://us.api.battle.net/wow/data/item/classes?locale=en_US&apikey=
wow_item_classes = {
    "classes": [{
        "class": 17,
        "name": "Battle Pets",
        "subclasses": [{
            "subclass": 0,
            "name": "BattlePet"
        }]
    }, {
        "class": 0,
        "name": "Consumable",
        "subclasses": [{
            "subclass": 5,
            "name": "Food & Drink"
        }, {
            "subclass": 0,
            "name": "Explosives and Devices"
        }, {
            "subclass": 1,
            "name": "Potion"
        }, {
            "subclass": 2,
            "name": "Elixir"
        }, {
            "subclass": 3,
            "name": "Flask"
        }, {
            "subclass": 7,
            "name": "Bandage"
        }, {
            "subclass": 9,
            "name": "Vantus Rune"
        }, {
            "subclass": 8,
            "name": "Other"
        }]
    }, {
        "class": 1,
        "name": "Container",
        "subclasses": [{
            "subclass": 4,
            "name": "Engineering Bag"
        }, {
            "subclass": 3,
            "name": "Enchanting Bag"
        }, {
            "subclass": 6,
            "name": "Mining Bag"
        }, {
            "subclass": 5,
            "name": "Gem Bag"
        }, {
            "subclass": 0,
            "name": "Bag"
        }, {
            "subclass": 2,
            "name": "Herb Bag"
        }, {
            "subclass": 1,
            "name": "Soul Bag"
        }, {
            "subclass": 8,
            "name": "Inscription Bag"
        }, {
            "subclass": 7,
            "name": "Leatherworking Bag"
        }, {
            "subclass": 10,
            "name": "Cooking Bag"
        }, {
            "subclass": 9,
            "name": "Tackle Box"
        }]
    }, {
        "class": 2,
        "name": "Weapon",
        "subclasses": [{
            "subclass": 173555,
            "name": "Melee Weapon"
        }, {
            "subclass": 174067,
            "name": "Melee Weapon"
        }, {
            "subclass": 41105,
            "name": "One-Handed Melee Weapon"
        }, {
            "subclass": 18,
            "name": "Crossbow"
        }, {
            "subclass": 19,
            "name": "Wand"
        }, {
            "subclass": 16,
            "name": "Thrown"
        }, {
            "subclass": 17,
            "name": "Spear"
        }, {
            "subclass": 20,
            "name": "Fishing Pole"
        }, {
            "subclass": 41617,
            "name": "One-Handed Melee Weapon"
        }, {
            "subclass": 3,
            "name": "Gun"
        }, {
            "subclass": 2,
            "name": "Bow"
        }, {
            "subclass": 1,
            "name": "Axe"
        }, {
            "subclass": 0,
            "name": "Axe"
        }, {
            "subclass": 7,
            "name": "Sword"
        }, {
            "subclass": 6,
            "name": "Polearm"
        }, {
            "subclass": 5,
            "name": "Mace"
        }, {
            "subclass": 4,
            "name": "Mace"
        }, {
            "subclass": 11,
            "name": "Bear Claws"
        }, {
            "subclass": 10,
            "name": "Staff"
        }, {
            "subclass": 9,
            "name": "Warglaives"
        }, {
            "subclass": 8,
            "name": "Sword"
        }, {
            "subclass": 15,
            "name": "Dagger"
        }, {
            "subclass": 14,
            "name": "Miscellaneous"
        }, {
            "subclass": 13,
            "name": "Fist Weapon"
        }, {
            "subclass": 12,
            "name": "Cat Claws"
        }, {
            "subclass": 1378,
            "name": "Two-Handed Melee Weapon"
        }, {
            "subclass": 262156,
            "name": "Ranged Weapon"
        }]
    }, {
        "class": 3,
        "name": "Gem",
        "subclasses": [{
            "subclass": 2,
            "name": "Strength"
        }, {
            "subclass": 1,
            "name": "Agility"
        }, {
            "subclass": 4,
            "name": "Spirit"
        }, {
            "subclass": 3,
            "name": "Stamina"
        }, {
            "subclass": 6,
            "name": "Mastery"
        }, {
            "subclass": 5,
            "name": "Critical Strike"
        }, {
            "subclass": 8,
            "name": "Versatility"
        }, {
            "subclass": 7,
            "name": "Haste"
        }, {
            "subclass": 10,
            "name": "Multiple Stats"
        }, {
            "subclass": 9,
            "name": "Other"
        }, {
            "subclass": 11,
            "name": "Artifact Relic"
        }, {
            "subclass": 0,
            "name": "Intellect"
        }]
    }, {
        "class": 4,
        "name": "Armor",
        "subclasses": [{
            "subclass": 0,
            "name": "Miscellaneous"
        }, {
            "subclass": 1,
            "name": "Cloth"
        }, {
            "subclass": 2,
            "name": "Leather"
        }, {
            "subclass": 3,
            "name": "Mail"
        }, {
            "subclass": 4,
            "name": "Plate"
        }, {
            "subclass": 5,
            "name": "Cosmetic"
        }, {
            "subclass": 6,
            "name": "Shield"
        }, {
            "subclass": 7,
            "name": "Libram"
        }, {
            "subclass": 8,
            "name": "Idol"
        }, {
            "subclass": 9,
            "name": "Totem"
        }, {
            "subclass": 10,
            "name": "Sigil"
        }, {
            "subclass": 11,
            "name": "Relic"
        }, {
            "subclass": 96,
            "name": "Shield"
        }]
    }, {
        "class": 5,
        "name": "Reagent",
        "subclasses": [{
            "subclass": 0,
            "name": "Reagent"
        }, {
            "subclass": 1,
            "name": "Keystone"
        }]
    }, {
        "class": 6,
        "name": "Tradeskill",
        "subclasses": [{
            "subclass": 3,
            "name": "Bullet"
        }, {
            "subclass": 2,
            "name": "Arrow"
        }]
    }, {
        "class": 7,
        "name": "Item Enhancement!",
        "subclasses": [{
            "subclass": 10,
            "name": "Elemental"
        }, {
            "subclass": 15,
            "name": "Weapon Enchantment - Obsolete"
        }, {
            "subclass": 16,
            "name": "Inscription"
        }, {
            "subclass": 5,
            "name": "Cloth"
        }, {
            "subclass": 6,
            "name": "Leather"
        }, {
            "subclass": 7,
            "name": "Metal & Stone"
        }, {
            "subclass": 8,
            "name": "Cooking"
        }, {
            "subclass": 9,
            "name": "Herb"
        }, {
            "subclass": 12,
            "name": "Enchanting"
        }, {
            "subclass": 4,
            "name": "Jewelcrafting"
        }, {
            "subclass": 1,
            "name": "Parts"
        }, {
            "subclass": 11,
            "name": "Other"
        }]
    }, {
        "class": 9,
        "name": "Recipe",
        "subclasses": [{
            "subclass": 0,
            "name": "Book"
        }, {
            "subclass": 1,
            "name": "Leatherworking"
        }, {
            "subclass": 2,
            "name": "Tailoring"
        }, {
            "subclass": 3,
            "name": "Engineering"
        }, {
            "subclass": 4,
            "name": "Blacksmithing"
        }, {
            "subclass": 5,
            "name": "Cooking"
        }, {
            "subclass": 6,
            "name": "Alchemy"
        }, {
            "subclass": 10,
            "name": "Jewelcrafting"
        }, {
            "subclass": 9,
            "name": "Fishing"
        }, {
            "subclass": 8,
            "name": "Enchanting"
        }, {
            "subclass": 7,
            "name": "First Aid"
        }, {
            "subclass": 11,
            "name": "Inscription"
        }]
    }, {
        "class": 11,
        "name": "Quiver",
        "subclasses": [{
            "subclass": 2,
            "name": "Quiver"
        }, {
            "subclass": 3,
            "name": "Ammo Pouch"
        }]
    }, {
        "class": 12,
        "name": "Quest",
        "subclasses": [{
            "subclass": 0,
            "name": "Quest"
        }]
    }, {
        "class": 13,
        "name": "Key",
        "subclasses": [{
            "subclass": 1,
            "name": "Lockpick"
        }, {
            "subclass": 0,
            "name": "Key"
        }]
    }, {
        "class": 15,
        "name": "Miscellaneous",
        "subclasses": [{
            "subclass": 4,
            "name": "Other"
        }, {
            "subclass": 3,
            "name": "Holiday"
        }, {
            "subclass": 2,
            "name": "Companion Pets"
        }, {
            "subclass": 1,
            "name": "Reagent"
        }, {
            "subclass": 0,
            "name": "Junk"
        }, {
            "subclass": 5,
            "name": "Mount"
        }]
    }, {
        "class": 16,
        "name": "Glyph",
        "subclasses": [{
            "subclass": 3,
            "name": "Hunter"
        }, {
            "subclass": 2,
            "name": "Paladin"
        }, {
            "subclass": 5,
            "name": "Priest"
        }, {
            "subclass": 4,
            "name": "Rogue"
        }, {
            "subclass": 1,
            "name": "Warrior"
        }, {
            "subclass": 11,
            "name": "Druid"
        }, {
            "subclass": 10,
            "name": "Monk"
        }, {
            "subclass": 12,
            "name": "Demon Hunter"
        }, {
            "subclass": 7,
            "name": "Shaman"
        }, {
            "subclass": 6,
            "name": "Death Knight"
        }, {
            "subclass": 9,
            "name": "Warlock"
        }, {
            "subclass": 8,
            "name": "Mage"
        }]
    }, {
        "class": 18,
        "name": "WoW Token",
        "subclasses": [{
            "subclass": 0,
            "name": "WoW Token"
        }]
    }]
}
