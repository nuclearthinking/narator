from TTS.api import TTS

import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2', progress_bar=True).to(device)
chapters = [
    ("""They spent a decent time skulking about in Venidse space. As one of the larger territories of the Vesia Kingdom, its vast space offered the Flagrant Vandals lots of desolate star systems to hide. For now, they hadn't seen hair nor hide of Venidse patrols.


There was a very good reason for that according to Iris.


"Do you think Venidse can become a worthy rival to Imodris without effort?" She began. "Imodris is closer to the core than Venidse. In addition, it jointly operates a strategically important port system. While the amount of wealth that flows through their hands can't match the trade that goes on in your famous Bentheim system, neither does the government siphon vast majority of wealth to subsidize the rest of the state."


Bentheim's wealth distribution was a fact of life to the Bright Republic. Otherwise, the Bentheim Liberation Movement wouldn't have grown so powerful and pervasive.


"So Venidse has to do something to match their rival in strength, then. You said that it's relatively well-endowed with resources. Is that enough to offset the trade that's captured by Imodris?"


"That's the complication. It's true that Venidse encompasses a lot of resource-rich star systems, but it takes a significant amount of labor and capital to extract them. That means people, equipment and bots."


Ves started to get an inkling of what she wanted to say. "The latter two is expensive, and relying too much on machines opens up a lot of vulnerabilities. So they have to rely a lot on labor as well."


"Living in Venidse isn't very charming. Aside from a couple of model planets, most of their planets are low-class hives where human lives are treated as valuable as cattle."


When he was young, the Bright Republic often showed how life in the Kingdom was awful for the lower classes. Their poorest had to toil in dangerous mines or spend endless hours supervising bots that did the exact same thing over and over again on the off-chance it glitched or caught a virus.


He recalled the city of Haston on Bentheim. That place was a concentration of the poorest on Bentheim and was a hotbed of BLM sympathy.


If Haston's circumstances magnified into entire planets, then Venidse's rebel group should be as powerful if not more than the BLM!


"The Venidse Liberators is one of the largest and most influential rebel movement in the Kingdom. Though they aren't particularly good at anything, they have access to a fair amount of resources and they are extremely numerous."


Ves paid a lot of attention to the fact that the VL accumulated a lot of resources. Perhaps that was why Major Verle chose to raid one of their facilities and trade with the rebel group during their passage through the territory.


"How powerful is Venidse's military?"


"Very powerful. Very numerous. I already told you about their mech doctrine. Since they have a lot of fingers in the resource extraction sector, they have the enviable ability to obtain much of their materials at near-cost price. This means they can fabricate more mechs at the same cost, which eventually accumulates into fielding more mech legions than any other territory."


"I see. It makes sense. A preference for attrition warfare can only be sustained if you have enough mechs to throw at the enemy." Ves said contemplatively.


"However, most of their numbers advantage is negated by the existence of the VL. The rebels have caused so much trouble over the decades that most of Venidse's military is burdened with guarding population centers, industries, mines and important installations. While that doesn't give us carte blanche to saunter in Vendise's space, we at least don't have to fight Venidse's troops every step of the way."


When Ves attended meetings with Major Verle and his staff, they all echoed the same refrain. Despite the might of Venidse's mech legions, they treated it as an opportunity to bounce back. The only point they argued about was deciding on which star system to raid.


Attacking a prosperous star system would go a long way in reducing their resource deficits. Attacking a less prominent planet came with a lot less risk as they didn't have to face any significant defenses.


Whatever the case, the Vandals only had enough time to attack a single star system. Attacking two systems at a time would delay their schedule and make them miss the two-month deadline.


Ves mostly stayed silent on this topic during the heated discussions in the conference room. He only provided some advice on which star system held the resources they needed and would be worthwhile to raid.


Up to now, Major Verle still hadn't made up his mind.


Besides taking part in those deadlocked discussions, Ves also began to make good on his promises by teaching the mech designers who worked hard enough to win a carrot. Predictably, most opted to borrow a valuable textbook from the central database, but one person happened to request personal tutelage.


"When I heard you wanted me to teach you, I was surprised." Ves said to Pierce over the projection. "If you wanted me to give you a few pointers, I would have given it for free."


Pierce shook his head. "I have my own pride, and I don't want to take advantage of you. Knowledge that comes free is not as sweet as knowledge that I've earned through my own efforts. My time learning the craft from my father has taught me that. I'm not as talented as you. I need to work for it. Otherwise, the knowledge won't stick."


Ves hadn't paid much attention to Pierce the past few days. They traveled on different ships, which made it inconvenient to chat with each other. In addition, Ves spent most of his time with Iris lately. The rebel-aligned mech designer was an attentive conversation partner who patiently brought him up to speed with regards to the Kingdom.


That said, he should have kept more in touch with Pierce. The Coalition-born mech designer had been assigned to the Beggar's Bounty, one of the two logistics ships of the task force. This was an important posting as Pierce had access to vastly more resources and facilities than anyone else. Though that made his work more complex, the man nonetheless persevered and exceeded his weekly quota.


Ves admired such dedication from his acquaintance, especially since he knew that Pierce was a rather mediocre mech designer.


His background as a mech designer from the Friday Coalition also held some promise. Though Ves did not need to establish any ties with his father, just his citizenship was valuable enough to open some doors that would be closed to a foreigner like Ves.


This was why Ves immediately changed his stance towards Pierce and beheld him with a bit more care.


"Well, you've earned the privilege of receiving my teachings fair and square. You'll get a full hour from me, which should be enough to solve most of your bottlenecks and burning questions. Don't waste it. While I'm proficient with most of the fundamentals, I happen to excel in Physics and lasers. So ask your questions."


Pierce dove into the questioning with glee. He started out with basic but tricky questions on multiple fields, and when he found out that Ves answered his questions without any effort, his questions began to encompass more and more complexity.


To Ves, answering the questions forced him to be thoughtful. As an Apprentice Mech Designer, Pierce wasn't stupid, and he didn't ask any stupid questions. Though the level of his questions didn't exceed the Journeyman-level, he nonetheless tread into territory that even Ves would pause at. All he could do was to use his superior Intelligence and Skills to churn out an answer on the spot.


At the end of the tutoring session, Pierce quickly excused himself from the call to digest the answers he received. Ves was left alone in his office to stew over the teaching session. Surprisingly, he enjoyed flexing his brain in this manner. There was something enjoyable about guiding a junior into understanding the problems that perplexed him for months or years.


"Heh." He chuckled. "Maybe I'll be a professor someday."


While he didn't feel too strongly about becoming a full-time teacher, he figured he could still treat it like a side activity. A lot of Journeymen and Seniors who owned successful businesses diverted some of their valuable time to teach at various universities and institutions. Obviously, they gained a lot of benefits for doing so. Since Ves happened to enjoy the act of teaching, he seriously started considering whether he should take a teaching position in the future.


"No one hires an Apprentice to teach at an institution. It's too soon for Journeymen to pass on their knowledge. I'll have to advance to Senior before I can become a respectable professor."


That would be a very long time away. Ves did not dare to predict when he would be able to advance to such an exalted rank, but it should at least be several decades away. Even with the help of the System, Ves did not belittle the difficulties involved with advancing past the vast majority of his peers. It wasn't easy to become a Journeyman, let alone a Senior.


"That is something to consider after this damned war is over. Right now, I've got to get back to work."


After the brief tutoring session, Ves returned to his duties. He checked with the mech technicians and made sure they didn't slack off on the job. He corresponded with his deputies and made sure they did the same. He liaised with Lieutenant Commander Soapstone and begged her to tap more into the task force's material reserves. He listened to the staff trying to argue which star system they should raid.


He also planned and supervised the repairs of the Inheritors. The good thing about the damaged Inheritors was that the skirmish with the Calico Dancer Bats didn't lead to a lot of material losses. Most of the damage the Inheritors sustained turned out to be self-inflicted as the lengthy twenty percent overload combined with the thirty percent spike led to a lot of internal disarray.


This meant that cables got fried or melted and circuits got heat-blasted. While that sounded bad and time-consuming to repair, Ves vastly preferred this type of internal damage because the Inheritors hadn't lost any materials. Fried components could easily be recycled and be used to fabricate new components.


The only issue was that it took a lot of time to effect the repairs. The damage ran throughout the entire interior of the frame, so every overloaded Inheritor mech pretty much required a complete disassembly. Otherwise, they wouldn't be able to repair or replace the innermost parts which happened to be the most vital ones that ensured the continued operation of the mechs.


All of this took time, too much time for them to adhere to the original timetable. Ves had to go back to the original planning and scrap some of the procedures he had in store just to make room for the unexpected repair work.


Naturally, the Inheritors that sustained actual battle damage required a bit more effort to bring them back into working capacity. The worst wrecks they retrieved from the battlefield were woefully incomplete or had been riddled with holes. To bring these Inheritors back online, the mech technicians demanded a lot of resources.


They didn't have enough to go around.


"We really need more resources, and they have to be the right ones as well."


The task force still carried valuable exotics and other materials in their cargo holds. Major Verle hoped to hold on to them until they reached a market system where they could dispose of their ill-gotten goods at fair market prices. Trading them away at this point wouldn't help the Vandals reduce their debt burden.


It was obvious that if the Major Verle didn't wish to give away their wealth to unscrupulous rebel traders, they urgently needed to get their needed supplies through another method.


After several days of uncertainty and procrastination, they finally decided on which star system they wanted to raid.""", 535),
    ("""The Shield of Hispania's conference room hosted a lot of contentious meetings lately. Ship captains, mech officers and staff officers all congregated in a single room to decide on which Venidse star system they should descend upon.


Everyone had their ideas. The hawks, which predominantly consisted of mech officers, wanted to raid a resource-rich system. Of course, they didn't aim their sights to systems comparable to the Detemen System. They couldn't afford to get bogged down by several hundred mechs.


The hawks picked out a number of targets that seemed very ambitious to Ves. Even if the Vandals rolled over the opposition, they would still pay a significant price.


The risk-averse crowd that comprised of other mech officers and the majority of the staff officers advocated for caution. The fleet was running low on certain resources, and they weren't at their best. Attacking a smaller, safer target should be the way to go.


These two groups had been at loggerheads for days. Ves watched on as the majority swung back and forth, all the while Major Verle showed uncharacteristic indecisiveness.


Ves was about Verle's stance. Throughout all of their time together, his impressions of the grizzled veteran had been as a staunch leader and a ruthless decision maker that wouldn't hesitate to take the most expedient course of action.


For him to withhold his decision at this junction puzzled Ves a little bit. Did he truly hesitate on his decision right now, or did he wish for the argument to play out?


His instincts believed that it must have been a deliberate choice. Ves mostly sat in the sidelines, so he could look at the entire situation with some detachment. Looking at the various officers attending the meetings via their projections while arguing passionately about their opinions, perhaps it all served as one giant distraction.


Every leader in the task force focused their energies into deciding which star system to raid. Some spent hours in research and preparation to present the most compelling arguments on why their targeted star systems was the most suitable ones to attack.


The momentous discussion distracted them from the misfortune they suffered in the past. Rather than allowing them to dwell at their failings, Verle sneakily used the meetings to direct his most important subordinates into thinking about their next steps forward.


Ves would have applauded the shrewd commanding officer if he wasn't afraid of giving the game away. He felt as if he constantly absorbed new tricks by staying in Major Verle's vicinity.


Eventually, the game had to come to an end. After yet another exhausting back-and-forth, Verle abruptly stood to announce his decision.


"We shall change course towards the Hachew System."


As expected, Major Verle chose to settle on a compromise. His answers didn't satisfy any of the participants, but it hadn't snubbed anyone either. An awkward atmosphere descended as everyone came to grips with the decision.


"The Hachew System isn't as well-defended as prosperous systems, but neither is it barren to the point of calling it a rural system. It hosts a moderate military presence and a handful of mines. Its value is nothing special, but it happens to extract some of the materials we are desperately short on. This should be sufficient to replenish some of our scarcity."


Ves quietly nodded as he read through the basic details of the Hachew System from the panel projected in the middle of the conference table. While it wouldn't enrich the Vandals and allow them to gain more trade goods for them to exchange for what they needed from the rebels, it did happen to contain some of the ores and materials that was vital in repairing and strengthening the Inheritor mechs.


The Hachew System actually looked like a destination that Ves would recommend himself if he didn't wish to refrain from taking part in the internal politics of the Flagrant Vandals.


"Prepare for battle. The Hachew System isn't very far away. Make sure our mechs are ready to deploy with as much strength as they can muster."


The task force had been drifting deeper into Venidse. It wouldn't take too much of a course change to reach the Hachew System. This told Ves that the entire show had been premeditated from the start. Major Verle already had a destination in mind before they even crossed into Venidse space!


Ves could tell that some of the other Vandals came to the same realization. However, they only amounted to twenty percent of the participants at most.


After the meeting came at an end, every projection winked out while those who were physically present left the compartment.


"Mr. Larkinson."


"Ah, yes sir?"


Major Verle walked up to him and asked an important question. "The next raid will require both spaceborn and landbound mechs. Can we field a sufficient amount of both at this stage?"


"Our spaceborn mech contingent requires more time to get back up to full strength. I'm sorry, but it will take at least two weeks to recover the majority of the Inheritors that sustained internal damage. The material damage was light but very comprehensive, so we have to rebuild them from the ground up. This is a necessary but time-consuming process. Even if you exhort my mech designers to work faster, it's unrealistic to expect them to be up and running in time for the Hachew raid."


The major furrowed his brows. "I did not anticipate the damage has reached such an extent. This isn't the first time we've overloaded the Inheritors. Every time, they bounced back fairly swiftly."


"I know, sir. I've browsed the archives. This is different, though. Previously, we had access to the Wolf Mother, which is an ad-hoc but fully functional factory ship. The production lines aboard that ship is capable of mass-producing an enormous amount of mech parts as long as we can feed enough materials into them. That's not possible now that we split up the main fleet. The two logistics ships our task force has retained can only do a fraction of the work of a factory ship."


To put it simply, the Verle Task Force got the short end of the stick when it came to the split. The Wolf Mother, Colonel Lowenfield, Major Verle and two of their remaining Journeyman Mech Designers had all been retained by the diminished main fleet that was on their way back to Republic space.


"Our landbound mechs?"


"They require a lot of repairs as well. We've never had the time to recover all of the damage our landbound mechs sustained in the Detemen Operation. It's been something of a low priority for us. According to our original schedule, we should have shifted more workers towards repairing the landbound mechs after crossing into Venidse. The destructive aftermath of the recent skirmish delayed that plan."


This put Major Verle in a worse position than he wished. Though the task force was still capable of fielding a respectable amount of spaceborn and landbound mechs, the shortages would hurt. Less mechs meant less reserves and a smaller margin for error.


Verle should have access to most of this information already. Ves was very punctual in his reports. It seemed to him that the man was desperate for hope.


Unfortunately for the both of them, Ves couldn't magically conjure up additional mechs. Hope didn't work that way.


"I will endeavor to ready as much mechs as possible in time for the raid, but don't expect too much from us, sir."


"We shall settle on that."


Ves walked away with a lot of uncertainty from that. The longer this trip progressed, the more he understood Verle's burden. Despite knowing little about the mech officer's history, he felt he became more in tune with Verle with each passing day.


The Hachew System shouldn't pose any threat to the Vandals. It was a system whose wealth sat between a rural system and an industrial system. In other words, wealthier than Cloudy Curtain but poorer than the Detemen System.


Unless Venidse predicted their destination beforehand, the Hachew System shouldn't be capable of inflicting heavy casualties to the Vandals.


Yet hadn't the LMC once trounced a Vesian raiding party?


"Don't underestimate the locals."


The Flagrant Vandals chose to raid the Hachew System because it held a number of strategically important mines to them. Any mine of value would be guarded. Fighting past these company forces was a nuisance at best, and a serious hindrance at worse.


"Besides the company forces, there's also reinforcements to consider."


The Vesians were still up in arms about their mortal enemy gallivanting in their space. Venidse might have felt a lot of schadenfreude when Imodris failed to stop the escaping Vandals from leaving their territory. Now that they ended up in Venidse space, the duchy couldn't afford to be as incompetent as Imodris back then. They would be hard at work trying to seek and destroy their vulnerable fleet.


The next couple of days, Ves threw himself into his work again. He exhorted his subordinates to speed up their repair work. Even one extra mech could make a lot of difference on the battlefield.


He even decided to pull up his own sleeves and perform some hands-on repairs of the most difficult cases aboard the Shield of Hispania. A lot of mech technicians looked perplexed when the head designer got his hands dirty, but Ves had been able to shorten a broken Inheritor's repairs in a single day where it took a full crew of mech technicians an entire week.


The work served as a nice distraction from the difficulties he had to deal with on a daily basis. That was also why he didn't show up again after repairing two of the most difficult mechs. It wasn't appropriate for him to devote all of his time to grunt work.


Back at his office, Ves got to play the manager. He juggled various responsibilities and priorities at once. All of this work and effort sent him into a contemplative mood.


"Is it worth it?"


Iris looked up again from her corner desk. "What's that, boss?"


"Do you ever think about how much effort we put in fabricating, selling, using, repairing and recycling mechs? How much money and resources are we expending on using mechs? The Flagrant Vandals alone are wasting billions of credits on an annual basis to maintain their strength. It's mind-boggling once you think about it. Are we working in vain?"


"I hope not." Iris furrowed her brow. "We're mech designers. If everyone stops using mechs, we'll all go out of business."


"The mech craze that has infected humanity four-hundred years ago is pretty much an artificial phenomenon. If not for the restriction on warships and the enforcement of the taboos, we would still be waging war with mighty ships."


"We would have been extinct by that time, sir. We were too eager with wiping out our own planets. I'm glad our race as a whole had managed to come together and agree to switch to mechs as a way to resolve our differences. We don't have to fear from genocidal maniacs anymore."


Ves shrugged at that. "All I'm saying is that there is a price for that. If you compare mechs to warships, which one do you think will prevail?"


He once witnessed a single small warships tearing apart a horde of spaceborn pirate mechs in the Glowing Planet campaign. That image of complete annihilation had been seared into his brain like a trauma that would never go away.


Ever since then, his faith in mechs had been cracked.


"Much of humanity has been proven to be too irresponsible for their own good. The intervention of the CFA and MTA was necessary to save our race from a spiral of destruction. Even they treated us as kids playing with fire, it's for the best."


"Being treated like children means we aren't allowed to grow up." Ves retorted. "It's been four-hundred years. I think we've learned enough lessons now. All of this mech warfare seems like play-acting to me sometimes."


Iris looked concerned. "Are you ill, sir? Do you need to visit the infirmary again? I've never heard of a mech designer who questions his own craft!"


"I don't know what's wrong with me either, but I'm not sick. I just have a premonition that the status quo can't go on forever. One day, the system will break."


Even without any solid proof, Ves believed what he said. Mechs were fine tools of war, but when it came down to it, a mech could never match the destruction that could be unleashed by a proper warship.


Some day, all of humanity had need of that destruction.

""", 536),
    (""""When we made plans to raid the Hachew System, I expected our mechs to batter the Vesians every step of the way." Ves spoke with a perplexed expression. "Rather than acting as the barbarians at the gates, I feel as if we are more like the tax collector coming to collect the annual tax."


When the Verle Task Force emerged out of FTL in the Hachew System, the local garrison immediately panicked. Instead of readying themselves to fight to the death, the outnumbered and outgunned defense squadron immediately fled to the nearest Lagrange point and transitioned to anywhere but here.


This allowed the Flagrant Vandals to waltz towards Hachew III, the only inhabited planet in the system. Once the combat carriers that conveyed their landbound mechs made landfall, they came across deserted cities, open warehouses and meagerly defended industries.


Not a single inhabitant took up arms to defend against the invaders. Without any signs of organized opposition, the Vandals practically acted with impunity on the surface of Hachew III!


While the Vandals remained alert and ready to switch to battle mode, there was also a palpable sense of ease running through their heads. Nobody in the command center seemed suspicious that they had entered a trap of sorts.


After slogging through the Detemen Operation and getting their butts kicked by the Calico Dancer Bats, Ves had a hard time trying to adjust to the lack of obstacles put in their way. What was it about the Hachew System that made them lose their will to fight?


"Iris?"


"It's simple, really. The ruler of Hachew III is Baron Imica of House Sabanet. His lineage isn't as long and storied as that of a count. His defense force only consists of three companies of spaceborn mechs and four companies of landbound mechs. Do you think that's a lot? The Flagrant Vandals can easily smash them apart, especially considering we are talking about garrison mechs!"


"Even then, it would benefit Venidse if House Sabanet puts up a fight. They're outnumbered, but not to the extent where we can win an instant victory. If they resort to harassment and guerilla warfare, they can easily ruin our raid."


"There's the key, boss. What does Baron Imica have to do with Venidse? The Duke of Venidse doesn't care about a tiny baron at all! Certainly, Baron Imica can order his household troops to put up a valiant fight against us, but what will that accomplish? Victory is impossible, and at worst he might lose all of the mechs he painstakingly funded over several decades. The Hachew System barely ekes out a profit for the house, so each mech is extraordinarily valuable to him. Unless he stands to gain more than he loses, Baron Imica will absolutely refuse to throw away his mechs to a lost cause."


"That's surprisingly rational of the baron." Ves remarked as if he had never seen a rational noble before. "Won't he get punished by Venidse?"


"Hah! No duke can compel a baron to send the foundation of his power into a suicide mission. Garrison mechs stand no chance against proper military mechs, and that's not taking into account that we outnumber them. Conserving your strength and denying us an easy victory is par for the course. At worst, House Sabanet will suffer a couple of years of disgrace and become a pariah in high society, but as long as they maintain their strength, they won't have to worry about their rivals deposing them from power."


Ves frowned at that. "This sounds as if House Sabanet are more wary of their domestic rivals than a foreign enemy."


"This raid is a one-off chance. The chances that Vandals will return to raid their planet again is practically nil. They've probably written off their material losses as a consequence from a massive freak accident. Wealth and goods is easy to replenish, but control over an entire planet is harder to regain when lost."


What Iris said probably rang true. The Vandal mechs that made landfall sauntered over the planet like they owned it. Though many industry complexes brandished their company forces, when push came to shove, the company goons retreated without firing a single shot.


The previous displays of intimidation always turned out to be bluffs. The company forces had orders to dissuade the Vandals from picking a fight with them, but because they were vastly outnumbered, their owners were loathe to throw them away in a senseless battle.


House Sabanet already set an example for the smaller players to follow. If the big guys refused to make a sacrifice, why should everyone else be selfless? It was every Vesian for themselves!


"Compared to foreign aggressors like you, their rivals are more immediate opponents to House Sabanet." Iris continued her explanation. "In the eyes of their neighbors, they want nothing more than see House Sabanet lose all of their mechs in a lopsided battle. Once the Vandals take their spoils and leave, the rivals can swoop in to claim Hachew III from the hands of the now-toothless House."


"That sounds really messed up. If House Sabanet sacrifices their mechs in battle against us, they should receive a commendation!"


"Who would give them their commendation? Hm? Mechs are expensive. Even Venidse can't magically compensate two-hundred mechs to a small baron on a whim. The games nobility play is a ruthless one. When it comes down to it, the best players don't care about duty, honor or accomplishments. They only care about how many mechs you can field and how hard it is to dislodge you from power. Even between liege lord and vassal, relations are frosty to the point where they won't hesitate to stab each other in the back when they can get away with such an act."


All of this neatly explained the cynical decision-making of the nobles who ruled the various demesnes of the Vesia Kingdom. The more Ves heard the details, the more he grew confused. "I don't understand. How can this mutual lack of trust even work? The more you explain it to me, the more I think of the Kingdom as an unwilling collection of selfish Houses."


"Ah, but that's exactly why the Kingdom still stands! Relations, connections, favors and rules all prop up its stability, but only at the surface. Underneath it all, friends can turn into enemies on a dime, favors can easily be forgotten and only the victors make the rules. The fundamental basis that allows a House to stand on their own is whether they possess the power to defend what is theirs. Newly enfeoffed nobles are often met with a rude awakening when they are first introduced in the ways the powerful play the game."


The sordid way the Kingdom ran its power plays made perverse sense to Ves, but he still couldn't quite adjust his mentality around this reality. "If every Vesian yields in front of the Vandals when they are coming to raid them, what stops us from taking advantage of it?"


"Oh, this is only because the Vandals are currently in the inner reaches of the Kingdom. Normally, these well-off territories are protected by the peripheral and border territories, so they never had to deal with any foreign raids. It's different at the border system. At first, these poor and struggling border systems yielded without a fight when the Vandals came to steal their riches. After doing it once, don't you think the Vandals will do it again?"


"So the Vandals actually took advantage of this?"


"Yup, up until the border systems wised up. Letting the Vandals treat them as their personal bank account was just encouraging them to suck all of their wealth away. Once they wised up and banded together, the Vandals could no longer roll over an under-defended star system. No matter how badly they were outnumbered, the garrison forces always fought as if their lives depended on it. This deterred the Vandals from raiding their systems with regularity."


It was much like how a bully pushed around someone weak for the first time. If the victim acquiesced to the bully and let them do whatever they wanted, the bully would just keep coming back and push even harder. Only by standing up would the bully have to contemplate whether it was worth it to push the victim again.


Evidently, the border systems had all become jaded enough to learn that they should never let anything go for free. Compared to the tough border systems, the star systems in the core territories of the Kingdom hadn't learned this lesson yet. They continued to obsess over their closest rivals and dismissed the threat of the Vandals!


Even though Ves had a lot of misgivings about this situation, he sobered up enough to take advantage of the lack of opposition. He helped guide the Vandals in picking out the best locations to raid. He felt like a kid entering the biggest toy store in the galaxy with an unlimited credit balance. The only limitation that restricted him from robbing the whole place blind was time.


They didn't have enough time. Even with the lack of fighting, they still couldn't afford to stick around for long before reinforcements arrived. Fortunately, the Hachew System wasn't close to any military strongholds.


After some time, Major Verle came to ask him a question. "Since we aren't facing any opposition in this raid, we are gathering much more goods than we projected. Will it be sufficient to meet all of our needs?"


Ves shook his head. "Far from it, sir. The stockpiles we are obtaining are very much needed, but they don't come in enough volume. I'd say we can only meet eighty percent of our current needs, and that is only with regards to these specific materials. We need other metals and compounds to round out our other needs. All in all, our supply situation looks a lot better now, but it's far from perfect."


"Hm. Once we are out of this star system, we'll be conducting a trade with the Venidse Liberators. I hope we can obtain some of what we need from them. It's going to be our only trade until we cross into Klein or Hafner."


They wouldn't trade much but the bare essentials, Ves knew. After a bit more talk, the major turned his attention to other matters, leaving Ves free to direct the raiding Vandals into pillaging more goods.


It felt rather strange for him to wield such power. Though the Vandals only treated his directions as suggestions, they placed so much faith in his judgement that he might as well be commanding them directly. His every decision decided whether a business survived or fell in this ordeal.


Sometimes, Ves had the illusion that he was playing god.


He didn't feel particularly guilty in ruining the Vesian businesses. Their states were at war, after all, and stripping and destroying each other's industries was as common as drinking water.


Perhaps this was what a proper raid looked like. Ves only had the botched Imodris Raid on the Mech Nursery and the Detemen Operation to go on. In both cases, the attackers and defenders fought with conviction. Here, Hachew III didn't even wait for the first blow to arrive before it collapsed.


Ves found the experience to be oddly hollow. There was a break in tradition. An imperfection in an otherwise perfect image. There should have been more fighting before they obtained their prize.


Was the Vesia Kingdom really so weak? The way the nobles distrusted each other practically weakened their state by half.


He would never want to live in this confusing and contradictory state. The Bright Republic might not be perfect, but Ves gained a new appreciation of how sane it was being run.


After an entire day of peaceful ransacking, their landbound mechs packed everything up and entered their combat carriers, which slowly ascended into space. Laden with much-needed resources and supplies, the invigorated Vandals leisurely disappeared from the hairs of House Sabanet after transitioning into FTL at a Lagrange point.

""", 537)
]

for text, chapter_number in chapters:
    model.tts_to_file(text, language='en', speaker_wav='neil_gaiman.wav', file_path=f'{chapter_number}.wav')
