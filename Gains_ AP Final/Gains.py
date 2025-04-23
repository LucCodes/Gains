# Libraries
from logging import root
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import turtle
import customtkinter

# https://stackoverflow.com/questions/21148471/on-python-how-do-i-determine-which-button-was-clicked

# Global Variables
global uBodyAnatomyList 
global uBodyTrainingList
global uBodyInjuryList
global lBodyAnatomyList 
global lBodyTrainingList
global lBodyInjuryList
global dietList
global supplementList

# Setup
root = customtkinter.CTk()
# root.iconbitmap("dumbbellicon.ico")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root.geometry("1005x470")
root.resizable(0, 0)
root.title('Gains: Strength and Hypertrophy')
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60)

# Upper Body Anatomy Order = Chest, Abdominal, Neck, Delt, Upper Back, Triceps, Biceps, Forearms
uBodyAnatomyList  = ["The Chest consists of two parts:\n \nPectoralis Major: Its major actions are adduction, or depression, of the arm and rotation of the arm forward about the axis of the body.\n \nPectoralis Minor: The primary actions of this muscle include the stabilization, depression, abduction or protraction, internal rotation and downward rotation of the scapula. It elevates the ribs for deep inspiration when the pectoral girdle is fixed or elevated.\n \nFrom: bodyweightlibary.com",
                    "The Abdominal consists of four parts:\n \nSerratus Anterior: The serratus anterior muscle pulls the scapula forward around the thorax, which allows for anteversion and protraction of the arm.\n \nExternal Oblique: The external oblique functions to pull the chest downwards and compress the abdominal cavity, which increases the intra-abdominal pressure as in a valsalva maneuver.\n \nRectus Abdominis: The main function of the rectus abdominis is to move the body between the ribcage and the pelvis.\n \nTendinous Inscriptions: The tendinous intersections, in conjunction with the rectus abdominis, function to provide varying degrees of forward flexion to the lumbar region of the vertebral column, producing forward bending at the waist.\n \nFrom: bodyweightlibary.com",
                    "The Neck consists of two parts:\n \nSternocleidomastoid: The sternocleidomastoid muscle is innervated by the accessory nerve. It is one of the largest and most superficial cervical muscles. The primary actions of the muscle are rotation of the head to the opposite side and flexion of the neck.\n \nTrapezius: The trapezius muscle is innervated by the accessory nerve. It is a large superficial muscle that extends longitudinally from the occipital bone to the lower thoracic vertebrae and laterally to the spine of the scapula.\n \nFrom: bodyweightlibary.com",
                    "The Deltoid muscle is responsible for the brunt of all arm rotation and allows a person to keep carried objects at a safer distance from the body. It is also tasked with stopping dislocation and injury to the humerus when carrying heavy loads.\n \nFrom: bodyweightlibary.com",
                    "The Upper Back consists of five parts:\n \nRhomboid Major: The rhomboid major helps to hold the scapula (and thus the upper limb) onto the ribcage.\nInfraspinatus: The infraspinatus muscle's action on the shoulder is primarily through its function as a rotator cuff muscle providing glenohumeral stability.\nTeres Major: The teres major is a medial rotator and adductor of the humerus and assists the latissimus dorsi in drawing the previously raised humerus downwards and backwards.\nTeres Minor: As a rotator cuff muscle, the teres minor stabilizes the ball-and-socket glenohumeral joint by helping hold the humeral head (ball) into the shallow glenoid cavity of the scapula (socket).\nLatissimus Dorsi: It functions to stabilize your back while extending your shoulders.\n \nFrom: bodyweightlibary.com",
                    "The Tricep consists of three parts (tri = three):\n \nLong head: The origin of the long head is the infra-glenoid tubercle of the scapula. Because it attaches to the scapula, the long head not only extends the elbow but will also have a small action on the glenohumeral or shoulder joint. With the arm adducted, the triceps muscle acts to hold the head of the humerus in the glenoid cavity. This action helps prevent any displacement of the humerus. The long head also assists with the extension and adduction of the arm at the shoulder joint. The lateral head is also active during the forearm extension at the elbow joint when the forearm is supinated or pronated.\n \nMedial Head: The origin of the medial head is at the dorsal humerus, inferior to the radial groove and connecting to the intermuscular septum. The medial head does not attach to the scapula and therefore has no action on the glenohumeral joint, whether with stabilization or movement. However, the medial head is active during the forearm extension at the elbow joint when the forearm is supinated or pronated.\n \nLateral Head: The lateral head originates at the dorsal humerus as well, but unlike the medial head, it is superior to the radial groove, where it fuses to the lateral intermuscular septum. This head is considered to be the strongest head of the three. It is active during the extension of the forearm at the elbow joint when the forearm is supinated or pronated.\n \nFrom: National Libary of Medicine",
                    "The Biceps consists of two parts:\nBrachialis: The brachialis is one of the largest elbow flexors and provides pure flexion of the forearm at the elbow.\n \nBiceps Brachii: Primary functions of the biceps brachii is flexion of the elbow and supination of the forearm. In fact, it is the prime mover of forearm supination.\n \nFrom: bodyweightlibary.com",
                    "The Forearm consists of 7 parts:\n \nFlexor Carpi Ulnaris: Together with other muscles of the anterior forearm, flexor carpi ulnaris flexes the hand at the wrist.\n \nBrachioradialis: The brachioradialis flexes the forearm at the elbow.\n \nPronator Teres: Pronator teres pronates the forearm, turning the hand posteriorly. If the elbow is flexed to a right angle, then pronator teres will turn the hand so that the palm faces inferiorly.\n \nExtensor Carpi Ulnaris: The extensor carpi ulnaris muscle is an elongated fusiform muscle located in the posterior compartment of the forearm and primarily functions to extend and adduct the wrist.\n \nFlexor Carpi Radialis: The main function of FCR is providing flexion of the wrist and assisting in abduction of the hand and wrist.\n \nPalmaris Longus: Palmaris longus synergistically works with the long flexors of the forearm to bring about flexion at the wrist joint and small joints of the hand.\n \nExtensor Pollicis Brevis: Together with extensor pollicis longus, extensor pollicis brevis is in charge of extension of the thumb in the first metacarpophalangeal joint.\n \nFrom: bodyweightlibary.com"
                    ]
uBodyTrainingList = ["Exercises:\n \nPec Dec Fly\nBench Press\nIncline Press\nDecline Press\nPush-Ups\nParallel Bar Dips\nDumbbell Presses\nDumbbell Flys\nIncline Dumbbell Presses\nIncline Flys\nCable Crossover Flys\nBumbbell Pullovers\nBarbell Pullovers\n \nNOTE: All Compound movements are usually done in a 4 set range, going light to start and going heavier each set. Accessory Movements are typically done in 3 sets of 12 repetitions",
                    "Examples of Abdominal Exercises:\n \nCrunches\nSit-Ups\nGym Ladder Sit-Ups\nCalves Over Bench Sit-Ups\nSuspended Bench Sit-Ups\nHigh-Pulley Crunches\nMachiene Crunches\nIncline Leg Raises\nLeg Raises\nHanging Leg Raises\nBroomstick Twists\nDumbbell Side Bends\nRoman Chair Side Bends",
                    "Many other execersies include the neck as support, meaning it is used almost everyday during a workout. The following exercises are ones that directly target the neck area:\n \nExercises:\n \nNeck Plank\nDumbbell Shrugs\nBarbell Shrugs",
                    "Examples of Delt Exercises:\n \nBack Press\nSeated Front Press\nSeated Dumbbell Press\nFront Dumbbell Press\nBent-Over Lateral Raises\nLateral Dumbbell Raises\nAlternate Front Arm Raises",
                    "Some Examples of Upper Back/Lat Exercises (Chris Bumstead's Back Routine):\n \nWide Neutral Grip Lat Pulldowns\nIncline Dumbbell Rows\nSingle Arm Chest Supported Rows\nSeated Rows\nReverse Grip Lat Pulldowns\nBanded Straight Arm Pulldowns",
                    "Some chest exercises actively train the tricep effectively. Most people train the tricep when also training the chest.\n \nExercises:\n \nLying Dumbbell Extentions\nTricep Dumbbell Kickback\nDiamond Push-Ups\nDips\nRope Tricep Extentions\nSkull Crushers\nClose Grip Bench Press\nDumbbell Overhead Extension",
                    "Many other execersies include the neck as support, meaning it is used almost everyday during a workout. The following exercises are ones that directly target the neck area:\n \nExercises:\n \nNeck Plank\nDumbbell Shrugs\nBarbell Shrugs",
                    "Exercises:\n \nDumbbell Wrist Flexion\nDumbbel Wrist Extension\nDumbbell Reverse Curl\nFarmer's Walk\nPull-Up Bar Hang\nTowel Pull-Up Hang\nWrist Twists\nWrist Curls\nReverse Wrist Curls\n \nFrom: Beachbody on Demand"
                    ]
uBodyInjuryList   = ["Most Common Chest Injury:\n \nPectoralis Major Tear: A pectoralis major lesion occurs when there is tearing of the pectoralis major muscle due to excessive tension on a maximally eccentrically contracted muscle or, less commonly, as a result of direct trauma. The injury most commonly occurs in young, physically active males in the third and fourth decades of life. It is often associated with weight lifting (particularly bench press), although there are reports of the injury during various other activities, such as martial arts, gymnastics, and football. It also has correlated with anabolic steroid use.\n \nFrom: National Libary of Medicine",
                    "Abdominal injuries in athletes can range in severity from abdominal strains to internal bleeding, and even insignificant injuries can prove to be incredibly painful. Therefore, the importance of the sports physical therapist's knowledge of abdominal injuries is imperative. The most medical professional in the stadium or arena must understand the signs and symptoms, possible risks, as well as the mechanism of injury of many of these common injuries in order to properly treat the athlete, and decide whether “proper treatment” is to hold them out of the game or transport them to emergency care. Abdominal injuries in the athlete are among the most potentially dangerous, and the importance of understanding these injuries cannot be understated.\n \nFrom: National Library of Medicine",
                    "A sprain of the ligaments or strain of the muscles in the neck can occur after an injury where the neck is bent or rotated (turned/twisted) in an abnormal way. Pain from a neck sprain, which can be mild or severe, does not always appear right away; you may not start to experience symptoms until hours after the injury, or even the next day. That is why you should see a doctor after a neck injury to get an evaluation even if you feel fine.\n \nFrom: Orthoinfo",
                    "Common sporting injuries of the shoulder include:\n \nDislocations, Acromioclavicular joint (ACJ) injuries, rotator cuff injuries, Labral tears, thrower's shoulder, biceps injuries, bursitis and fractures.\n \nFrom: ShoulderDoc",
                    "Twisting or pulling a muscle or tendon can result in a strain. It can also be caused by a single instance of improper lifting or by overstressing the back muscles. A chronic (long-term) strain usually results from overuse after prolonged, repetitive movement of the muscles and tendons. A sprain often occurs after a fall or sudden twist, or a blow to the body that forces a joint out of its normal position. All of these conditions stretch one or more ligaments beyond their normal range of movement, causing injury.\n \nFrom: Cleveland Clinic",
                    "Tricep Tendonitis: Weightlifter’s elbow, also known in medical terms as triceps tendonitis, can cause significant discomfort and make many everyday activities challenging. Tendonitis is also called tendinitis.\n \nTricep Tendon Rupture: A rupture or tear in the triceps tendon, the tendon that connects the triceps muscle to the elbow, can result in the tendon becoming detached from the bone. This injury can be very painful and debilitating.\n \nFrom: Florida Orthopaedic Institute, Upswing Health",
                    "Bicep Tear or Strain: A bicep strain or tear is caused by excess strain on the shoulder due to overuse. The most common symptom of a bicep tear or strain is pain in the upper arm, which can lead to bruising, muscle spasms, or loss of mobility and strength\n \nBicep Tendonitis: Tendonitis can occur because of repetitive motion. For instance, professional baseball players, swimmers, tennis players and golfers are at risk for tendonitis in their shoulders, arms and elbows. Tendonitis can also occur because of a sudden, serious load to the tendon.\n \nFrom: Bon Secours, Cleveland Clinic",
                    "Injury to the forearm usually results from trauma secondary to, for example, a fall, a road traffic accident or a sporting injury. It can also result from overuse. Injuries include muscle strain and contusion, crush injuries, fractures and tendon and nerve injuries.\n \nFrom: Patient UK"
                    ]

# Lower Body Anatomy Order = Thighs, Hamstrings, Calfs, Glutes, Lower Back
lBodyAnatomyList  = ["The Thighs consists of 8 parts:\n \nTensor Fasciae Latae: The tensor fasciae latae works in synergy with the gluteus medius and gluteus minimus muscles to abduct and medially rotate the femur.\n \nRectus Femoris: It is a two way acting muscle as it crosses over the hip and knee joint; therefore, it contributes to 90° of knee flexion and assists iliopsoas in hip flexion.\n \nVastus Lateralis: This muscle is the largest of the quadriceps which includes: rectus femoris, vastus intermedius, and vastus medialis. Together, the quadriceps act on the knee and hip to promote movement as well as strength and stability.\n \nPectineus: Its physiologic role is in the flexing and adducting (drawing inward toward the body) of the thigh.\n \nAdductor Longus: One of the adductor muscles of the hip, its main function is to adduct the thigh and it is innervated by the obturator nerve.\n \nGracilis: The muscle adducts, medially rotates (with hip flexion), laterally rotates, and flexes the hip as above, and also aids in flexion of the knee.\n \nSartorius: The sartorius muscle can move the hip joint and the knee joint, but all of its actions are weak, making it a synergist muscle.\n \nVastus Medialis: This muscle is used to extend the leg at the knee and to stabilize the patella, which is also known as the kneecap.\n \nFrom: bodyweightlibary.com",
                    "The hamstrings are a group of three muscles which predominantly act to flex the knee. Hamstrings consist of 3 muscles; Semitendinosus, Semimembranosus, and Biceps femoris. The muscles cross two joints and have long proximal and distal tendons with resultant long muscle tendon junctions (MTJ). MTJs extend into the muscle bellies, overlap within the muscle belly, facilitate transmission and dissipate forces across the MTJ while muscle contraction and relaxation.\n \nFrom: Physiopedia",
                    "The Test consists of 7 parts:\n \nPeroneus Brevis: The Peroneus Brevis is responsible for 63% of the power needed to evert the foot as well as assists in plantar flexion along with the Peroneus Longus.\n \nTibialis Anterior: It plays an important role in the activities of walking, hiking and kicking the ball by stabilizing the ankle joint as the foot hits the floor and pull it clear of the ground as the leg continues moving.\n \nFlexor Hallucis Longus: the flexor hallucis longus muscle functions to plantar flex and invert the foot. However, it is unique in that it also functions to flex the great toe and helps supinate the ankle.\n \nPeroneus Longus: This muscle serves to move your foot and ankle in various directions.\n \nSoleus: The action of the calf muscles, including the soleus, is plantarflexion of the foot.\n \nGastrocnemius: Its function is plantar flexing the foot at the ankle joint and flexing the leg at the knee joint.\n \nExtensor Digitorum Longus: This muscle allows you to extend your toes (bend them upward) and dorsiflex your feet (bend them upward through the ankle joint).\n \nFrom: bodyweightlibary.com",
                    "The Glutes consists of 2 parts:\n \nGluteus Medius: Gluteus medius is the prime mover of abduction at hip joint. Anterior portion of Gluteus medius abduct, assist in flexion and medial rotation of hip.\n \nGluteus Maximus: Gluteus maximus main actions are to extend and laterally rotate the hip joint. Furthermore, upper fibers can abduct the hip whereas the lower fibers can adduct.\n \nFrom: bodyweightlibary.com"
                    ]
lBodyTrainingList = ["Exercises:\n \nSquats\nLeg Press\nHip Abductions\nLeg Extensions\nDeadlift\nSplit Squats\nLunges\nHack Squats\nWall Sits\nBox Squats",
                    "Exercises:\n \nRomainian Dead Lifts(RDLs)\nLeg Curl\nLaying Hamstring Curl\nSquats\nDeadlifts\nBulgarian Split Squats\nSingle-Leg Deadlifts",
                    "Exercises:\n \nCalf Raises\nCalf Press\nCalf Extension\nStanding Calf Raise\nToe Raises",
                    "Exercises:\n \nHip Thrust\nBulgarian Split Squats\nGlute Bridge\nDeadlift\nSquats\nGood Mornings\nHip Abduction"
                    ]
lBodyInjuryList   = ["Common Thigh Injuries:\n \nHip Flexor Strain: The hip flexors are a group of muscle located at the front of the hip and assist with lifting the leg (i.e. marching motion). Injuries can be due to inactivity (i.e. sedentary occupation), overuse (i.e. playing sport) or sudden trauma (i.e. leg suddenly slipping backwards). This can give rise to pain and stiffness over the front of the thigh and groin.\n \nIliopsoas Bursitis: A bursa is a fluid filled sac found in areas of the body where a tendon or muscle rubs over a bone. The function of a bursa is to decrease the amount of friction, if the bursa becomes inflamed it can swell causing compression and pain in the surrounding anatomical structures. Behind the iliopsoas muscle lies a large burse, this decreases the friction between the muscle and pelvic bone. Repeated running and kicking motions can give rise to irritation and inflammation of the bursa. Symptoms can include a deep ache into the front of the hip and groin, pain with lifting the leg (i.e. marching position), snapping sensation, pain with crossing the legs.\n \nAdductor Tendinopathy/Groin Strain: The groin muscles attach onto the pelvis via a tendon. Inflammation and thinning of this tendon can lead to tissue tears. This can be due to overuse (i.e. playing sport) or sudden trauma (i.e. suddenly lunging sideways, leg slipping out sideways). Symptoms can include pain over the groin and inner thigh, pain with side stepping, bringing the legs together and marching movements, pain during and after activity and difficulty pivoting and changing directions.\n \nFrom: My Family Physio",
                    "A hamstring injury involves straining or pulling one of the hamstring muscles — the group of three muscles that run along the back of the thigh. Hamstring injuries often occur in people who play sports that involves sprinting with sudden stops and starts. Examples include soccer, basketball, football and tennis. Hamstring injuries can occur in runners and in dancers as well.\n \nFrom: Mayo Clinic",
                    "Pulled Calf Muscle: A pulled calf muscle occurs when you overstretch the muscles in the back of your lower leg. Also called calf muscle strains, this injury can involve mild overstretching or complete tearing of the muscle. Mild injuries usually improve with rest, ice, compression and elevation. A torn calf muscle may require surgery.\n \nFrom: Cleveland Clinic",
                    "Gluteal Injuries:  A gluteal contusion is a bruise to the muscle area. A gluteal muscle strain is a stretch or partial tear of the muscle or tendon. Trauma, either by a fall or a direct blow to the buttock area, causes most gluteal injuries.\n \nFrom: MedicineNet"
                    ]

# Diet Order = Calories, Protein, Carb, Fats, Cutting, Bulking
dietList = ["The amount of energy in an item of food or drink is measured in calories. When we eat and drink more calories than we use up, our bodies store the excess as body fat. If this continues, over time we may put on weight. As a guide, an average man needs around 2,500kcal (10,500kJ) a day to maintain a healthy body weight.\n \n From: NHS",
            "What is Protein?:\n \nProtein is found throughout the body—in muscle, bone, skin, hair, and virtually every other body part or tissue. It makes up the enzymes that power many chemical reactions and the hemoglobin that carries oxygen in your blood. At least 10,000 different proteins make you what you are and keep you that way. Protein is made from twenty-plus basic building blocks called amino acids. Because we don’t store amino acids, our bodies make them in two different ways: either from scratch, or by modifying others. Nine amino acids—histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, tryptophan, and valine—known as the essential amino acids, must come from food.\n \nHow much protein do you need?:\n \nFor bodybuilders, you should be cosuming 0.8-1.5 grams of protein per pound you weigh.\n \nFrom: Harvard Health\n \nSome foods that are high in protein include:\n \nChicken\nBeef\nFish\nEggs\nMilk\nCheese\nYogurt\nBeans\nNuts\nTofu\nQuinoa\n ",
            "What are Carbohydrates?:\n \nCarbohydrates are found in a wide array of both healthy and unhealthy foods—bread, beans, milk, popcorn, potatoes, cookies, spaghetti, soft drinks, corn, and cherry pie. They also come in a variety of forms. The most common and abundant forms are sugars, fibers, and starches. Foods high in carbohydrates are an important part of a healthy diet. Carbohydrates provide the body with glucose, which is converted to energy used to support bodily functions and physical activity.\n \nFrom: Harvard Health\n \nSome foods that are high in carbohydrates include:\n \nBread\nPasta\nRice\nPotatoes\nBeans\nFruits\nVegetables\n ",
            "What are Fats?:\n \nWhen it comes to dietary fat, what matters most is the type of fat you eat. Contrary to past dietary advice promoting low-fat diets, newer research shows that healthy fats are necessary and beneficial for health. When food manufacturers reduce fat, they often replace it with carbohydrates from sugar, refined grains, or other starches. Our bodies digest these refined carbohydrates and starches very quickly, affecting blood sugar and insulin levels and possibly resulting in weight gain and disease. Findings from the Nurses’ Health Study and the Health Professionals Follow-up Study show that no link between the overall percentage of calories from fat and any important health outcome, including cancer, heart disease, and weight gain. Rather than adopting a low-fat diet, it’s more important to focus on eating beneficial “good” fats and avoiding harmful “bad” fats. Fat is an important part of a healthy diet. Choose foods with “good” unsaturated fats, limit foods high in saturated fat, and avoid “bad” trans fat.",
            "A cutting diet reduces a person's calorie intake to lose body fat while maintaining muscle mass. Cutting diets typically prioritize lean proteins, nutrient-dense vegetables, and whole grains. Bodybuilders and fitness enthusiasts often use a cutting diet after a bulking phase to achieve a leaner physique.\n \nFrom: Healthline",
            "A bulking diet focuses on nutrient- and calorie-dense foods. These stimulate controlled weight gains to enhance muscle building, whereas a cutting diet includes nutrient-dense, lower calorie foods to stimulate fat loss and muscle maintenance.\n \nFrom: Healthline"
            ]

# Supplement Order = Energy, Muscle, Testosterone, Fat Loss
supplementList = ["Energy supplementaion is used by millions, or even billions around the whole world. These supplements can help fight fatigue and tiredness. Energy supplementation should be taken carefully, with it there could be many problems with them if you overconsume them. Always ask your doctor before taking any type of supplement. Here are the most popular energy supplements:\n \nCaffiene\nThe eight B vitamins\nGuarana\nCoenzyme Q10",
                "Certain dietary supplements can help you achieve desired muscle growth results, regardless of whether your ultimate goal is to compete in a bodybuilding competition or simply be stronger and more active in everyday life.\n \nFrom: Forbes Health\n \nSome of these supplemtns include: \n \nWhey Protein Powder\nCreatine\nHMB\nEAAs\nBeta Alanine",
                "There is many natural supplements to boost your testosterone, but most 'Booster's' is a marketing gimmick. The best supplements you can use to actually boost your T is herbal, with most notable being Tongkat Ali. Other's include Ashwaganda, Honey, Garlic, Moringa, and Maca Root",
                "When you want to drop some weight, it's tempting to look for help anywhere you can. If your thoughts turn to supplements or herbal remedies, keep in mind that research gives many of them mixed reviews. In some cases, there isn't a lot of science to back up the claims, and some have health risks. Supplements are not regulated by the FDA in the same way that food and drugs are. The FDA does not review these supplements for safety or efficacy before they hit the market. Also, you should know that the FDA has cracked down on some weight loss supplements that had prescription drugs in them that weren't noted on the label. You can't always tell what you're getting. Talk with your doctor first before you try any.\n \n From: WebMD\n \nSome Supplements include:\n\nYohimbine\nL-Carnitine\nGreen Tea Extract\nCaffine\n"
                ]

# Window Functions

def upperBodyWindows(bodyPart):
    # Setup
    bodyFrame = customtkinter.CTkFrame(master=root, width=1005, height=470)
    button._set_appearance_mode("Dark")

    listPos     = ''
    anatomyList = ["Chest", "Abdominal", "Neck", "Deltoid", "Upper Back", "Triceps", "Biceps", "Forearms"]
    for i in range(len(anatomyList)):
        if bodyPart == anatomyList[i]:
            listPos = i
            break
    
    if listPos != '':
        anatomyTextVal  = str(uBodyAnatomyList[listPos])
        trainingTextVal = str(uBodyTrainingList[listPos])
        injuryTextVal   = str(uBodyInjuryList[listPos])
        
        # Anatomy Description
        AnatomyText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
        AnatomyText.place(x = 680, y = 80)
        AnatomyText.insert("0.0", anatomyTextVal)
        AnatomyText.configure(state="disabled")
        
        # Labels
        TrainingLabel = customtkinter.CTkLabel(root, text="Training", font = ('Verdana', 20), fg_color="#303030")
        TrainingLabel.place(x=360, y = 50)
        AnatomyLabel = customtkinter.CTkLabel(root, text="Anatomy", font = ('Verdana', 20), fg_color="#303030")
        AnatomyLabel.place(x=680, y = 50)
        InjuriesLabel = customtkinter.CTkLabel(root, text="Injuries", font = ('Verdana', 20), fg_color="#303030")
        InjuriesLabel.place(x = 30, y = 50)
        
        # Muscle Growth Description
        TrainingText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
        TrainingText.place(x = 360, y = 80)
        TrainingText.insert("0.0", trainingTextVal)
        TrainingText.configure(state="disabled")
        bodyFrame.place(x = 5, y = 10)
        
        # Possible Injuries Descrition
        InjuriesText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
        InjuriesText.place(x = 30, y = 80)
        InjuriesText.insert("0.0", injuryTextVal)
        InjuriesText.configure(state="disabled")
        bodyFrame.place(x = 5, y = 10)
        
        # Back Button and Destruction
        bodyDestroy     = bodyFrame.destroy
        TextDestroy     = AnatomyText.destroy
        TrainingDestroy = TrainingText.destroy
        InjuriesDestroy = InjuriesText.destroy
        TLabelDestroy   = TrainingLabel.destroy
        AlabelDestroy   = AnatomyLabel.destroy
        ILabelDestroy   = InjuriesLabel.destroy
        
        Back = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Back", command = lambda: [ILabelDestroy(), AlabelDestroy(), TLabelDestroy(), bodyDestroy(), TextDestroy(), TrainingDestroy(), InjuriesDestroy()], font = ('Verdana', 15))
        Back.place(x = 850, y = 450)
    return

def lowerBodyWindows(bodyPart):
    # Setup
    bodyFrame = customtkinter.CTkFrame(master=root, width=1005, height=470)
    button._set_appearance_mode("Dark")
    
    listPos     = ''
    anatomyList = ["Thighs", "Hamstrings", "Calfs", "Glutes"]
    for i in range(len(anatomyList)):
        if bodyPart == anatomyList[i]:
            listPos = i
            break
    
    if listPos != '':
        anatomyTextVal  = str(lBodyAnatomyList[listPos])
        trainingTextVal = str(lBodyTrainingList[listPos])
        injuryTextVal   = str(lBodyInjuryList[listPos])
        
        # Anatomy Description
        AnatomyText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
        AnatomyText.place(x = 680, y = 80)
        AnatomyText.insert("0.0", anatomyTextVal)
        AnatomyText.configure(state="disabled")
        
        # Labels
        TrainingLabel = customtkinter.CTkLabel(root, text="Training", font = ('Verdana', 20), fg_color="#303030")
        TrainingLabel.place(x=360, y = 50)
        AnatomyLabel = customtkinter.CTkLabel(root, text="Anatomy", font = ('Verdana', 20), fg_color="#303030")
        AnatomyLabel.place(x=680, y = 50)
        InjuriesLabel = customtkinter.CTkLabel(root, text="Injuries", font = ('Verdana', 20), fg_color="#303030")
        InjuriesLabel.place(x = 30, y = 50)
        
        # Muscle Growth Description
        TrainingText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
        TrainingText.place(x = 360, y = 80)
        TrainingText.insert("0.0", trainingTextVal)
        TrainingText.configure(state="disabled")
        bodyFrame.place(x = 5, y = 10)
        
        # Possible Injuries Descrition
        InjuriesText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
        InjuriesText.place(x = 30, y = 80)
        InjuriesText.insert("0.0", injuryTextVal)
        InjuriesText.configure(state="disabled")
        bodyFrame.place(x = 5, y = 10)
        
        # Back Button and Destruction
        bodyDestroy     = bodyFrame.destroy
        TextDestroy     = AnatomyText.destroy
        TrainingDestroy = TrainingText.destroy
        InjuriesDestroy = InjuriesText.destroy
        TLabelDestroy   = TrainingLabel.destroy
        AlabelDestroy   = AnatomyLabel.destroy
        ILabelDestroy   = InjuriesLabel.destroy
        
        Back = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Back", command = lambda: [ILabelDestroy(), AlabelDestroy(), TLabelDestroy(), bodyDestroy(), TextDestroy(), TrainingDestroy(), InjuriesDestroy()], font = ('Verdana', 15))
        Back.place(x = 850, y = 450)
    return

def supplementWindows(supplementType):
    # Setup
    supplementFrame = customtkinter.CTkFrame(master=root, width=1005, height=470)
    
    listPos = ''
    supplementTypeList = ["Energy", "Muscle", "Testosterone", "Fat Loss"]
    for i in range(len(supplementTypeList)):
        if supplementType == supplementTypeList[i]:
            listPos = i
            break
        
    # Labels
    supplementLabel = customtkinter.CTkLabel(root, text=supplementType, font = ('Verdana', 20), fg_color="#303030")
    supplementLabel.place(x=360, y = 50)
    
    # Energy Supplements Description
    supplementText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
    supplementText.place(x = 360, y = 80)
    supplementText.insert("0.0", str(supplementList[listPos]))
    supplementText.configure(state="disabled")
    supplementFrame.place(x = 5, y = 10)
    
    # Back Button and Destruction
    frameDestroy = supplementFrame.destroy
    textDestroy  = supplementText.destroy
    labelDestroy = supplementLabel.destroy
    Back = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Back", command = lambda: [textDestroy(), labelDestroy(), frameDestroy()], font = ('Verdana', 15))
    Back.place(x = 850, y = 450)
    return

def dietWindows(dietType):
    # Setup
    dietFrame = customtkinter.CTkFrame(master=root, width=1005, height=470)

    listPos      = ''
    dietTypeList = ["Calories", "Protein", "Carbs", "Fats", "Cutting", "Bulking"]
    for i in range(len(dietTypeList)):
        if dietType == dietTypeList[i]:
            listPos = i
            break
    
    dietLabel = customtkinter.CTkLabel(root, text=dietType, font = ('Verdana', 20), fg_color="#303030")
    dietLabel.place(x=360, y = 120)
    
    if listPos != '':
        # Calories Description
        dietText = customtkinter.CTkTextbox(root, width=380, height= 150, text_color="#8B8378", wrap=WORD)
        dietText.place(x = 360, y = 150)
        dietText.insert("0.0", str(dietList[listPos]))
        dietText.configure(state="disabled")
        dietFrame.place(x = 5, y = 10)
        
        # Back Button and Destruction
        frameDestroy = dietFrame.destroy
        textDestroy  = dietText.destroy
        labelDestroy = dietLabel.destroy
        Back = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Back", command = lambda: [textDestroy(), labelDestroy(), frameDestroy()], font = ('Verdana', 15))
        Back.place(x = 850, y = 450)
    return

# Helper Functions
    
def LBackWindow():
    # Setup
    LBackFrame = customtkinter.CTkFrame(master=root, width=1005, height=470)
    # Labels
    StrengthingLabel = customtkinter.CTkLabel(root, text="Strengthing", font = ('Verdana', 20), fg_color="#303030")
    StrengthingLabel.place(x=360, y = 50)
    InjuriesLabel = customtkinter.CTkLabel(root, text="Injuries", font = ('Verdana', 20), fg_color="#303030")
    InjuriesLabel.place(x = 30, y = 50)
    # Muscle Strengthing Description
    TrainingText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
    TrainingText.place(x = 360, y = 80)
    TrainingText.insert("0.0", "Although you can't nesscessarily grow your lower back, it can be beneficial to strengthen it. Many people suffer from lower back pain, espically lifters after years go by. There are some exercises that can help strengthen and prevent lower back pain, as seen here:\n \nSupine Bridge\nBird Dog\nCat Camel\nChild's Pose\nKnee-to-strech Stretch")
    TrainingText.configure(state="disabled")
    LBackFrame.place(x = 5, y = 10)
    # Possible Injuries Descrition
    InjuriesText = customtkinter.CTkTextbox(root, width=300, height= 250, text_color="#8B8378", wrap=WORD)
    InjuriesText.place(x = 30, y = 80)
    InjuriesText.insert("0.0", "Lumbar (lower back) muscle strains and sprains are the most common causes of low back pain. Muscle strains and sprains are common in the lower back, because it supports the weight of the upper body and is involved in moving, twisting and bending.\n \nFrom:American Association of Neurological Surgeons")
    InjuriesText.configure(state="disabled")
    LBackFrame.place(x = 5, y = 10)
    # Back Button and Destruction
    TestDestroy = LBackFrame.destroy
    TrainingDestroy = TrainingText.destroy
    InjuriesDestroy = InjuriesText.destroy
    SLabelDestroy= StrengthingLabel.destroy
    ILabelDestroy = InjuriesLabel.destroy
    Back = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Back", command = lambda: [ILabelDestroy(), SLabelDestroy(), TestDestroy(), TrainingDestroy(), InjuriesDestroy()], font = ('Verdana', 15))
    Back.place(x = 850, y = 450)

def calculate_bmi():
    try:
        weight       = float(weight_entry.get())
        heightFeet   = float(height_entry_ft.get())
        heightInches = float(height_entry_in.get())
        height       = float(heightFeet) * 12 + float(heightInches)
        bmi          = (weight / (height * height)) * 703
        bmiValue.insert(0, str(bmi))
    except Exception as ex:
        print(ex)

# Make Some Gains
GainsLetter = customtkinter.CTkLabel(root, text="MAKE SOME GAINS", font = ('Verdana', 25))
GainsLetter.place(x=700, y = 400)

# # Gain Logo
# GainLogo = ImageTk.PhotoImage(Image.open("logo.png"))
# Glabel   = Label(frame, image = GainLogo)
# Glabel.pack()

# Titles for Front and Back Buttons + UI Frame
leftframe = customtkinter.CTkFrame(root, fg_color="#303030", width=340, height=240)
leftframe.place(x = 5, y = 10)

rightframe = customtkinter.CTkFrame(root, fg_color="#303030", width=340, height=160)
rightframe.place(x = 660, y = 10)

dietframe = customtkinter.CTkFrame(root, fg_color="#303030", width=340, height=200)
dietframe.place(x = 660, y = 180)

suppsframe = customtkinter.CTkFrame(root, fg_color="#303030", width=340, height=200)
suppsframe.place(x = 5, y = 260)

bmiframe = customtkinter.CTkFrame(root, fg_color="#303030", width=300, height=195)
bmiframe.place(x = 353, y = 265)

Upperlabel = customtkinter.CTkLabel(root, text="Upper Body", font = ('Verdana', 20), fg_color="#303030")
Upperlabel.place(x=120, y = 10)

Lowerlabel = customtkinter.CTkLabel(root, text="Lower Body", font = ('Verdana', 20), fg_color="#303030")
Lowerlabel.place(x=770, y = 10)

DietLabel = customtkinter.CTkLabel(root, text="Diet", font = ('Verdana', 20), fg_color="#303030")
DietLabel.place(x=805, y = 180)

SuppsLabel =  customtkinter.CTkLabel(root, text="Supplementation", font = ('Verdana', 20), fg_color="#303030")
SuppsLabel.place(x=90, y = 260)

BMILabel =  customtkinter.CTkLabel(root, text="BMI Calculator", font = ('Verdana', 20), fg_color="#303030")
BMILabel.place(x=430, y = 265)

# Upper Muscle Buttons
upperBodyInfo = [["Chest", 30, 50], ["Abdominal", 180, 50], ["Neck", 30, 90], ["Upper Back", 100, 130], ["Deltoid", 180, 90], ["Triceps", 30, 170], ["Biceps", 180, 170], ["Forearms", 100, 210]]
for bodyInfo in upperBodyInfo:
    bodyPart, xPos, yPos = bodyInfo
    button = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text=bodyPart, font = ('Verdana', 15), command = lambda m = bodyPart: upperBodyWindows(m))
    button.place(x=xPos, y=yPos)

# Lower Muscle Buttons
lowerBodyInfo = [["Thighs", 690, 50], ["Hamstrings", 840, 50], ["Calfs", 690, 90], ["Glutes", 840, 90]]
for bodyInfo in lowerBodyInfo:
    bodyPart, xPos, yPos = bodyInfo
    button = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text=bodyPart, font = ('Verdana', 15), command = lambda m = bodyPart: lowerBodyWindows(m))
    button.place(x=xPos, y=yPos)

LowerBackButton = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Lower Back", font = ('Verdana', 15), command = LBackWindow)
LowerBackButton.place(x = 760, y = 130)

# Diet Buttons
dietInfo = [["Calories", 760, 220], ["Protein", 690, 260], ["Carbs", 840, 260], ["Fats", 760, 300], ["Cutting", 690, 340], ["Bulking", 840, 340]]
for diet in dietInfo:
    dietType, xPos, yPos = diet
    button = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text=dietType, font = ('Verdana', 15), command = lambda m = dietType: dietWindows(m))
    button.place(x=xPos, y=yPos)

# Supplementation Buttons
supplementInfo = [["Energy", 30, 300], ["Muscle", 180, 300], ["Testosterone", 180, 340], ["Fat Loss", 30, 340]]
for supplement in supplementInfo:
    supplementType, xPos, yPos = supplement
    button = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text=supplementType, font = ('Verdana', 15), command = lambda m = supplementType: supplementWindows(m))
    button.place(x=xPos, y=yPos)

SuppsText = customtkinter.CTkTextbox(root, width=300, height= 80, text_color="#8B8378", wrap=WORD)
SuppsText.place(x = 30, y = 375)
SuppsText.insert("0.0", "Although Supplementation isn't required to increase strength or hypertrophy, it could be beneficial for some.")
SuppsText.configure(state="disabled")
 
# BMI Calculator

# Weight
weight_label = customtkinter.CTkLabel(root, text = "Weight(Pounds):", fg_color="#303030")
weight_label.place(x = 356, y = 290)
weight_entry = customtkinter.CTkEntry(root, width = 37, height=2)
weight_entry.place(x = 600, y = 295)

# Height Feet
height_label_ft = customtkinter.CTkLabel(root, text = "Height(ft):", fg_color="#303030")
height_label_ft.place(x = 356, y = 320)
height_entry_ft = customtkinter.CTkEntry(root, width = 37, height=2)
height_entry_ft.place(x = 600, y = 323)

# Height Inches
height_label_in = customtkinter.CTkLabel(root, text = "Height(in):", fg_color="#303030")
height_label_in.place(x = 356, y = 350)
height_entry_in = customtkinter.CTkEntry(root, width = 37, height=2)
height_entry_in.place(x = 600, y = 353)

# Calculate Button
BMIButton = customtkinter.CTkButton(root, fg_color="#3D3D3D", hover_color="blue", text="Calculate", font = ('Verdana', 15), command = calculate_bmi)
BMIButton.place(x = 430, y = 380) 

# BMI Text Result
bmi_label = customtkinter.CTkLabel(root, text = "BMI:", fg_color="#303030")
bmi_label.place(x = 356, y = 420)
bmiValue = customtkinter.CTkEntry(root, width = 37, height=2)
bmiValue.place(x = 600, y = 423)

root.mainloop()

# dumbbell icon from https://icon-icons.com/
# symbol from: https://www.vecteezy.com/free-vector/gym-logo