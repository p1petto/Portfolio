import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3

Window {
    id:win;
    width: 360
    height: 640
    minimumWidth: 360
    minimumHeight: 640
    visible: true
    title: qsTr("Loyouts")
    Item{
        anchors.fill:parent
        id: container
        ColumnLayout{
            anchors.fill:parent
            spacing:0

            Line_Bar{
                id: head
                Layout.alignment: Qt.AlignTop
                height: win.height / 9

                Item{
                    width: content.width
                    height: content.height
                    anchors.centerIn: parent
                    RowLayout{
                        anchors.fill:parent
                        spacing:10
                        Backspace{
                            opacity: 0
                            id: backspace
                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    if (container.state === "pressed_second") {
                                        container.state = "pressed_first";
                                    } else if (container.state === "pressed_third") {
                                        container.state = "pressed_second";
                                    }
                                }
                            }
                        }
                    }
                    Text {
                        id: textHeader
                        text: "header"
                        anchors.centerIn: parent
                    }
                }
            }
            Rectangle {
                id: body
                color: 'gainsboro'
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.alignment: Qt.AlignLeft
                Block{
                    width: parent.width * 0.96
                    height: parent.height * 0.96
                    id: content
                    comText: "content"

                }
            }
            Line_Bar{
                id: foot
                anchors.top: body.bottom
                height: win.height / 9

                RowLayout{
                    anchors.fill:parent
                    spacing:10
                    Bt {
                        id: bt_first
                        comText: "1"
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                container.state = "pressed_first";
                            }
                        }

                    }
                    Bt {
                        id: bt_second
                        comText: "2"
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                container.state = "pressed_second";
                            }
                        }

                    }
                    Bt {
                        id: bt_third
                        comText: "3"
                        MouseArea {
                            anchors.fill: parent
                            onClicked: {
                                container.state = "pressed_third";
                            }
                        }
                    }

                }


            }


        }

        states:[
            State {
                name: "pressed_first"
                PropertyChanges {target: bt_first; comColorText:"black"}
                PropertyChanges {target:bt_second; comColorText:"#666670"}
                PropertyChanges {target:bt_third;  comColorText:"#666670"}

                PropertyChanges {target: bt_first; comColor:"#b3b3b3"}
                PropertyChanges {target: bt_second; comColor:"#A5A5A5"}
                PropertyChanges {target: bt_third; comColor:"#A5A5A5"}

                PropertyChanges {target:content;  comText:"Pressed first"}
                PropertyChanges {target:textHeader;  text:"Pressed first"}

                PropertyChanges {target:backspace;  opacity:0}
            },
            State {
                name: "pressed_second"
                PropertyChanges {target: bt_first; comColorText:"#666670"}
                PropertyChanges {target:bt_second; comColorText:"black"}
                PropertyChanges {target:bt_third;  comColorText:"#666670"}

                PropertyChanges {target: bt_first; comColor:"#A5A5A5"}
                PropertyChanges {target: bt_second; comColor:"#b3b3b3"}
                PropertyChanges {target: bt_third; comColor:"#A5A5A5"}

                PropertyChanges {target:content;  comText:"Pressed second"}
                PropertyChanges {target:textHeader;  text:"Pressed second"}

                PropertyChanges {target:backspace;  opacity:1}

            },
            State {
                name: "pressed_third"
                PropertyChanges {target: bt_first; comColorText:"#666670"}
                PropertyChanges {target:bt_second; comColorText:"#666670"}
                PropertyChanges {target:bt_third;  comColorText:"black"}

                PropertyChanges {target: bt_first; comColor:"#A5A5A5"}
                PropertyChanges {target: bt_second; comColor:"#A5A5A5"}
                PropertyChanges {target: bt_third; comColor:"#b3b3b3"}

                PropertyChanges {target:content;  comText:"Pressed third"}
                PropertyChanges {target:textHeader;  text:"Pressed third"}

                PropertyChanges {target:backspace;  opacity:1}
            } ]
        transitions:[
            Transition {
                from: "*"
                to: "*"
                PropertyAnimation{
                    target:bt_first
                    property: "comColor"
                    duration: 200}
                PropertyAnimation{
                    target:bt_second
                    property: "comColor"
                    duration: 200}
                PropertyAnimation{
                    target:bt_third
                    property: "comColor"
                    duration: 200}
                PropertyAnimation {
                    target:backspace
                    property: "opacity"
                    duration: 200}
            }]

    }

}



